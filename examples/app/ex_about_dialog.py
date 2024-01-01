import logging
import sys

from PySide6 import QtWidgets

from hyo2.abc2.app.app_info import AppInfo
from hyo2.abc2.app.app_style import AppStyle
from hyo2.abc2.app.dialogs.about.about_dialog import AboutDialog
from hyo2.abc2.lib.lib_info import LibInfo
from hyo2.abc2.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

app = QtWidgets.QApplication(sys.ar)
AppStyle.apply(app=app)

d = AboutDialog(lib_info=LibInfo(), app_info=AppInfo(), with_locale_tab=True, with_gdal_tab=True)
d.show()

sys.exit(app.exec_())
