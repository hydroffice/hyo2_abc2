import logging
import sys

from PySide6 import QtWidgets

from hyo2.abc2.app.app_style.app_style import AppStyle
from hyo2.abc2.app.pkg_info import app_info
from hyo2.abc2.app.pkg_info.pkg_info_tab import PkgInfoTab
from hyo2.abc2.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

app = QtWidgets.QApplication(sys.argv)
AppStyle.apply(app)

mw = QtWidgets.QMainWindow()

t = PkgInfoTab(
    main_win=mw,
    app_info=app_info,
    with_online_manual=True,
    with_offline_manual=True,
    with_bug_report=True,
    with_hydroffice_link=True,
    with_ccom_link=True,
    with_noaa_link=True,
    with_unh_link=True,
    with_license=True
)
t.show()

sys.exit(app.exec())
