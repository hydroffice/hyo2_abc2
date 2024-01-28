import logging
import sys
from PySide6 import QtWidgets

from hyo2.abc2.app.app_style.app_style import AppStyle
from hyo2.abc2.app.noaa_support.noaa_s57_dialog import NOAAS57Dialog
from hyo2.abc2.app.pkg_info import app_info
from hyo2.abc2.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

app = QtWidgets.QApplication(sys.argv)
AppStyle.apply(app)

d = NOAAS57Dialog(app_info=app_info)
d.show()

sys.exit(app.exec())
