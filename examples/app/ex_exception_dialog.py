import sys
import logging

from PySide6 import QtWidgets

from hyo2.abc2.app.dialogs.exception.exception_dialog import ExceptionDialog
from hyo2.abc2.lib.lib_info import LibInfo
from hyo2.abc2.app.app_info import AppInfo
from hyo2.abc2.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

app = QtWidgets.QApplication([])

d = ExceptionDialog(lib_info=LibInfo(), app_info=AppInfo())
d.show()

sys.exit(app.exec())
