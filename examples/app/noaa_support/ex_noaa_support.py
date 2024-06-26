import logging
from PySide6 import QtWidgets

from hyo2.abc2.app.qt_progress import QtProgress
from hyo2.abc2.app.noaa_support.noaa_support import NOAASupport
from hyo2.abc2.app.pkg_info import app_info
from hyo2.abc2.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

delete_local_folder = False
copy_files = True

QtWidgets.QApplication([])
w = QtWidgets.QWidget()
w.show()

noaa_support = NOAASupport(app_info=app_info, progress=QtProgress(parent=w))


if noaa_support.internal_zip_path_exists():
    internal_zip_path = noaa_support.internal_zip_path()
    logger.debug("internal zip: %s" % internal_zip_path)

    success = noaa_support.unzip_internal_zip()
    logger.debug("installed internal zip: %s" % success)
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
