import logging
import os
import re
import requests
import traceback
from urllib.parse import urlparse, parse_qs

from tqdm import tqdm
from bs4 import BeautifulSoup

from hyo2.abc2.lib.progress.abstract_progress import AbstractProgress
from hyo2.abc2.lib.progress.cli_progress import CliProgress

logger = logging.getLogger(__name__)


class GoogleDrive:
    CHUNK_SIZE = 32768  # 32KiB

    def __init__(self, show_progress: bool = False, debug_mode: bool = False, progress: AbstractProgress = None) \
            -> None:
        if debug_mode:
            self.debug_level = 2
        else:
            self.debug_level = 0

        self.show_progress = show_progress
        self.chunk_count = None
        self.filesize = None
        self.file_count = None
        self.file_nr = None
        if progress is None:
            self.progress = CliProgress()
        else:
            self.progress = progress

    @classmethod
    def extract_file_id(cls, url_or_id: str) -> str:
        """Extract the file ID from a Drive share URL or return the input if it looks like an ID."""
        # If it already looks like an ID (simple heuristic)
        if re.fullmatch(r"[a-zA-Z0-9_-]{10,}", url_or_id):
            return url_or_id

        # try to parse common Drive URL formats
        # patterns:
        #  - https://drive.google.com/file/d/<id>/view...
        #  - https://drive.google.com/open?id=<id>
        #  - https://drive.google.com/uc?id=<id>&export=download
        parsed = urlparse(url_or_id)
        qs = parse_qs(parsed.query)
        if "id" in qs:
            return qs["id"][0]

        m = re.search(r"/d/([a-zA-Z0-9_-]+)", url_or_id)
        if m:
            return m.group(1)

        # last resort: try to find an id-like substring
        m = re.search(r"([a-zA-Z0-9_-]{10,})", url_or_id)
        if m:
            return m.group(1)

        raise ValueError("Could not extract a Google Drive file id from input")

    def download_from_google(self, file_id: str, file_name: str, target: str = "."):
        """
        Downloads a file from Google Drive, handling potential confirmation tokens for large files.
        """
        # First try: docs.google.com/uc?export=download&id=FileID
        base_url = "https://docs.google.com/uc"
        session = requests.Session()
        params = {
            "export": "download",
            "id": file_id
        }
        response = session.get(base_url, params=params, stream=True)

        # If Content-Disposition is present, the file is directly available
        if "content-disposition" not in response.headers:
            # Try to get the token from cookies
            token = None
            for k, v in response.cookies.items():
                if k.startswith("download_warning"):
                    token = v
                    break

            # If no token in cookies, extract it from the HTML
            if not token:
                soup = BeautifulSoup(response.text, "html.parser")
                # Common case: HTML contains a form with id="download-form"
                download_form = soup.find("form", {"id": "download-form"})
                if download_form and download_form.get("action"):
                    # Extract action URL, which might be drive.usercontent.google.com/download
                    download_url = download_form["action"]
                    # Collect all hidden inputs
                    hidden_inputs = download_form.find_all("input", {"type": "hidden"})
                    form_params = {}
                    for inp in hidden_inputs:
                        if inp.get("name") and inp.get("value") is not None:
                            form_params[inp["name"]] = inp["value"]

                    # Re-send the GET request with these parameters
                    response = session.get(download_url, params=form_params, stream=True)
                else:
                    # Otherwise, search for confirm=xxx in HTML
                    match = re.search(r'confirm=([0-9A-Za-z-_]+)', response.text)
                    if match:
                        token = match.group(1)
                        # Include the confirm token in the request
                        params["confirm"] = token
                        response = session.get(base_url, params=params, stream=True)
                    else:
                        raise Exception(
                            "Unable to find the download link or confirmation token in the response. Download failed.")

            else:
                # Use the token obtained from cookies and resend the request
                params["confirm"] = token
                response = session.get(base_url, params=params, stream=True)

        # Ensure the download directory exists
        os.makedirs(target, exist_ok=True)
        file_path = os.path.join(target, file_name)

        # Start downloading the file in chunks, with a progress bar
        try:
            total_size = int(response.headers.get('content-length', 0))
            if self.show_progress:
                self.progress.start(text="Downloading", has_abortion=True)

            with open(file_path, "wb") as f, tqdm(
                    desc=file_name,
                    total=total_size,
                    unit="B",
                    unit_scale=True,
                    unit_divisor=1024,
            ) as bar:
                token = GoogleDrive.CHUNK_SIZE / total_size * 90.0
                for chunk in response.iter_content(chunk_size=self.CHUNK_SIZE):
                    if chunk:
                        f.write(chunk)
                        bar.update(len(chunk))
                        self.progress.add(token)

            if self.show_progress:
                self.progress.end()
            logger.debug(f"File successfully downloaded to: {file_path}")

        except Exception as e:
            raise Exception(f"File download failed: {e}")

    def get_file(self, file_src: str, file_dst: str, unzip_it: bool = False) -> None:

        file_dst = os.path.abspath(file_dst)
        if os.path.exists(file_dst):
            os.remove(file_dst)

        fid = self.extract_file_id(url_or_id=file_src)
        logger.info(f"Downloading file {fid} ...")
        target = os.path.dirname(file_dst)
        file_name = os.path.basename(file_dst)
        self.download_from_google(file_id=fid, target=target, file_name=file_name)
        logger.info(f"Downloading file {fid} ... DONE")

        if unzip_it:
            import zipfile

            try:
                z = zipfile.ZipFile(file_dst, "r")

                unzip_path = os.path.dirname(file_dst)

                logger.debug("unzipping %s to %s" % (file_dst, unzip_path))

                name_list = z.namelist()
                self.file_nr = len(name_list)
                if self.show_progress:
                    self.progress.start(text="Unzipping", has_abortion=True)

                self.file_count = 0
                for item in name_list:
                    # print(item)
                    z.extract(item, unzip_path)
                    self.file_count += 1
                    if self.show_progress:
                        if self.progress.canceled:
                            raise RuntimeError("unzip stopped by user")
                        pct = int((self.file_count / self.file_nr) * 100.0)
                        self.progress.update(pct)
                z.close()
                os.remove(file_dst)
                if self.show_progress:
                    self.progress.end()

            except Exception as e:
                traceback.print_exc()
                raise RuntimeError("unable to unzip the downloaded file: %s -> %s" % (file_dst, e))
