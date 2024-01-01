import sys
import logging

from PySide6 import QtWidgets

from hyo2.abc2.app.tabs.info.info_tab import InfoTab
from hyo2.abc2.app.app_style import AppStyle
from hyo2.abc2.lib.lib_info import LibInfo
from hyo2.abc2.app.app_info import AppInfo
from hyo2.abc2.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

app = QtWidgets.QApplication(sys.argv)
AppStyle.apply(app)

mw = QtWidgets.QMainWindow()

t = InfoTab(main_win=mw,
            lib_info=LibInfo(), app_info=AppInfo(),
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
