import logging
import os.path

from hyo2.abc2.lib.logging import set_logging
from hyo2.abc2.lib.testing import Testing
from hyo2.abc2.lib.googledrive import GoogleDrive

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

onedrive_link = r"https://drive.google.com/file/d/1ie1_hNH4EbAJ51mReLj_a6KJmZUimR1H/view?usp=sharing"

tp = Testing()
zip_path = os.path.join(tp.output_data_folder(), "test.zip")
unzip_path = os.path.join(tp.output_data_folder(), "test.txt")

if os.path.exists(zip_path):
    os.remove(zip_path)
if os.path.exists(unzip_path):
    os.remove(unzip_path)

gd = GoogleDrive(show_progress=True, debug_mode=True)
gd.get_file(file_src=onedrive_link, file_dst=zip_path, unzip_it=True)

if os.path.exists(unzip_path):
    with open(unzip_path) as fid:
        text = fid.read().strip()
        if text == "test":
            logger.debug(text)
