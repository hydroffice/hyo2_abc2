import logging

from hyo2.abc2.lib.logging import set_logging
from hyo2.abc2.lib.package.pkg_helper import PkgHelper

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

folder_path = r"C:\code\hyo2\hyo2_grids"

filter_files = (
    r"desktop.ini",
)
filter_folders = (
    r"__pycache__",
)

PkgHelper.clean_folder(folder=folder_path, filter_files=filter_files, filter_folders=filter_folders)
