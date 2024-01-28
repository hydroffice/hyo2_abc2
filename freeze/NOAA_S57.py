import os
import sys

from PySide6 import QtWidgets, QtGui

from hyo2.abc2.app.app_style.app_style import AppStyle
from hyo2.abc2.app.pkg_info import app_info
from hyo2.abc2.lib.logging import set_logging
from hyo2.abc2.app.noaa_support.noaa_s57_dialog import NOAAS57Dialog

set_logging(ns_list=["hyo2.abc2", ])

app = QtWidgets.QApplication([])
app.setApplicationName('NOAA S57')
app.setOrganizationName("HydrOffice")
app.setOrganizationDomain("hydroffice.org")
AppStyle.apply(app=app)

d = NOAAS57Dialog(app_info=app_info)
d.setWindowIcon(QtGui.QIcon(os.path.join(app_info.app_media_path, "noaa_support.png")))
d.show()

sys.exit(app.exec())
