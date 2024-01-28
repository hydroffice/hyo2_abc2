import logging
import sys

from PySide6 import QtWidgets

from hyo2.abc2.app.pkg_info import app_info
from hyo2.abc2.app.app_style.app_style import AppStyle
from hyo2.abc2.app.pkg_info.pkg_about.pkg_about_dialog import PkgAboutDialog
from hyo2.abc2.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

app = QtWidgets.QApplication(sys.argv)
AppStyle.apply(app=app)

dlg = PkgAboutDialog(app_info=app_info, with_locale_tab=True, with_gdal_tab=True)
dlg.show()

sys.exit(app.exec())
