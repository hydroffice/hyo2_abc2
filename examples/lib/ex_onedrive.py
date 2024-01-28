import logging
import os.path

from hyo2.abc2.lib.logging import set_logging
from hyo2.abc2.lib.testing import Testing
from hyo2.abc2.lib.onedrive import OneDrive

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

# onedrive_link = r"https://universitysystemnh-my.sharepoint.com/:u:/g/personal/" \
#                 r"gma72_usnh_edu/EaMqI1w9pplDsqCapeqJYYgBo0LP8CqHnkyXlDKkoHeBLg?e=4MEVzV&download=1"
onedrive_link = r"https://universitysystemnh-my.sharepoint.com/:u:/g/personal/" \
                r"gma72_usnh_edu/ET4kv3t8CuBGuyHUqThonvMBMmxWp5f3ZTt08XG_u9COHQ?e=mVEJij&download=1"

root_folder = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
tp = Testing(root_folder=root_folder)
file_dst = os.path.join(tp.output_data_folder(), "onedrive.zip")

od = OneDrive(show_progress=True, debug_mode=True)
od.get_file(file_src=onedrive_link, file_dst=file_dst, unzip_it=True)
