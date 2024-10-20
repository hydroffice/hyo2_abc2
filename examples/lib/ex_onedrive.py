import logging
import os.path

from hyo2.abc2.lib.logging import set_logging
from hyo2.abc2.lib.testing import Testing
from hyo2.abc2.lib.onedrive import OneDrive

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

onedrive_link = r"https://universitysystemnh-my.sharepoint.com/:u:/g/personal/" \
                r"gma72_usnh_edu/EabgRi9pTtdEvIVDXoEXHOYBH4FBHtN07i_8VkjpAAstYQ?e=Wn7q98&download=1"

root_folder = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
tp = Testing(root_folder=root_folder)
zip_path = os.path.join(tp.output_data_folder(), "test.zip")
unzip_path = os.path.join(tp.output_data_folder(), "test.txt")

if os.path.exists(zip_path):
    os.remove(zip_path)
if os.path.exists(unzip_path):
    os.remove(unzip_path)

od = OneDrive(show_progress=True, debug_mode=True)
od.get_file(file_src=onedrive_link, file_dst=zip_path, unzip_it=True)

if os.path.exists(unzip_path):
    with open(unzip_path) as fid:
        text = fid.read().strip()
        if text == "test":
            logger.debug(text)
