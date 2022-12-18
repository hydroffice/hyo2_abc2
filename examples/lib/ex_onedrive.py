import logging
import os.path
from pathlib import Path

from hyo2.abc2.lib.logging import set_logging
from hyo2.abc2.lib.testing_paths import TestingPaths
from hyo2.abc2.lib.onedrive import OneDrive

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

# onedrive_link = r"https://universitysystemnh-my.sharepoint.com/:u:/g/personal/" \
#                 r"gma72_usnh_edu/EaMqI1w9pplDsqCapeqJYYgBo0LP8CqHnkyXlDKkoHeBLg?e=4MEVzV&download=1"
onedrive_link = r"https://universitysystemnh-my.sharepoint.com/:u:/g/personal/" \
                r"gma72_usnh_edu/ET4kv3t8CuBGuyHUqThonvMBMmxWp5f3ZTt08XG_u9COHQ?e=mVEJij&download=1"

file_dst = os.path.join(TestingPaths(root_folder=Path(__file__).parent.parent.parent.resolve()).output_data_folder(),
                        "onedrive.zip")

od = OneDrive(show_progress=True, debug_mode=True)
od.get_file(file_src=onedrive_link, file_dst=file_dst, unzip_it=True)
