import logging
import os
import sys
from PySide6 import QtWidgets, QtGui

from hyo2.abc2.app.dialogs.noaa_s57.noaa_s57 import NOAAS57Dialog
from hyo2.abc2.lib.lib_info import LibInfo
from hyo2.abc2.app.app_info import AppInfo
from hyo2.abc2.app.app_style import AppStyle

logger = logging.getLogger()


def set_logging(default_logging=logging.WARNING, hyo2_logging=logging.INFO, abc_logging=logging.DEBUG):
    logging.basicConfig(
        level=default_logging,
        format="%(levelname)-9s %(name)s.%(funcName)s:%(lineno)d > %(message)s"
    )
    logging.getLogger("hyo2").setLevel(hyo2_logging)
    logging.getLogger("hyo2.abc2").setLevel(abc_logging)


set_logging()

app = QtWidgets.QApplication([])
app.setApplicationName('NOAA S57')
app.setOrganizationName("HydrOffice")
app.setOrganizationDomain("hydroffice.org")
app.setStyleSheet(AppStyle.load_stylesheet())

d = NOAAS57Dialog(lib_info=LibInfo(), app_info=AppInfo())
d.setWindowIcon(QtGui.QIcon(os.path.join(AppInfo().app_media_path, "noaa_support.png")))
d.show()

sys.exit(app.exec_())
