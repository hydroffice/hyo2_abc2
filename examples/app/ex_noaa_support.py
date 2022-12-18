import logging
from PySide6 import QtWidgets

from hyo2.abc2.app.qt_progress import QtProgress
from hyo2.abc2.app.dialogs.noaa_s57.noaa_support import NOAASupport
from hyo2.abc2.lib.lib_info import LibInfo
from hyo2.abc2.app.app_info import AppInfo
from hyo2.abc2.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

use_setup = 0  # 0: internal, 1: NOAA, 2: CCOM
delete_local_folder = False
copy_files = True

QtWidgets.QApplication([])
w = QtWidgets.QWidget()
w.show()

noaa_support = NOAASupport(lib_info=LibInfo(), app_info=AppInfo(), progress=QtProgress(parent=w))

if use_setup == 0:

    if noaa_support.internal_zip_path_exists():
        internal_zip_path = noaa_support.internal_zip_path()
        logger.debug("internal zip: %s" % internal_zip_path)

        success = noaa_support.unzip_internal_zip()
        logger.debug("installed internal zip: %s" % success)
        if not success:
            exit(-1)


elif use_setup == 1:  # 5.8 is now 7z, thus this fails

    success = noaa_support.download_from_noaa()
    logger.debug("download from noaa: %s" % success)
    if not success:
        exit(-1)

elif use_setup == 2:  # 5.8 not uploaded

    success = noaa_support.download_from_unh()
    logger.debug("download from unh: %s" % success)
    if not success:
        exit(-1)

noaa_support.open_local_noaa_support_folder()

if not noaa_support.local_noaa_support_folder_present():
    exit(-1)

logger.debug("Local folder present: %s" % noaa_support.local_noaa_support_folder())
logger.debug("Local version: %s" % noaa_support.local_noaa_support_folder_version())

bat_exists = noaa_support.check_local_batch_file_exists()
if bat_exists:
    logger.debug("local batch file: %s" % noaa_support.local_batch_file)

if delete_local_folder:
    noaa_support.delete_local_noaa_support_files()
    exit()

if copy_files:

    system_noaa_support_folder = noaa_support.system_noaa_support_folder()
    logger.debug("system folder: %s" % system_noaa_support_folder)
    if noaa_support.system_noaa_support_folder_present():
        logger.debug("system version: %s" % noaa_support.system_noaa_support_folder_version())
        noaa_support.delete_system_noaa_support_files()

    noaa_support.copy_local_to_system()
    logger.debug("system batch file: %s" % noaa_support.system_batch_file())

    noaa_support.exec_system_batch()