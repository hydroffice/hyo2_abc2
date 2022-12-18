import sys
import os
from PySide6 import QtWidgets, QtGui

from hyo2.abc2.lib.lib_info import LibInfo
from hyo2.abc2.app.app_info import AppInfo
from hyo2.abc2.app.app_style import AppStyle
from hyo2.abc2.app.dialogs.noaa_s57.noaa_s57 import NOAAS57Dialog
from hyo2.abc2.lib.logging import set_logging


set_logging(ns_list=["hyo2.abc2", ])

app = QtWidgets.QApplication([])
app.setApplicationName('NOAA S57')
app.setOrganizationName("HydrOffice")
app.setOrganizationDomain("hydroffice.org")
AppStyle.apply(app=app)

d = NOAAS57Dialog(lib_info=LibInfo(), app_info=AppInfo())
d.setWindowIcon(QtGui.QIcon(os.path.join(AppInfo().app_media_path, "noaa_support.png")))
d.show()

sys.exit(app.exec())
