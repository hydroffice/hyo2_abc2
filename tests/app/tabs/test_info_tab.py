import unittest
import platform

from PySide6 import QtCore, QtWidgets, QtTest

# import logging
# logging.basicConfig(level=logging.DEBUG)

from hyo2.abc2.app.tabs.info.info_tab import InfoTab
from hyo2.abc2.lib.lib_info import LibInfo
from hyo2.abc2.app.app_info import AppInfo


class TestAppTabsInfoTab(unittest.TestCase):

    @unittest.skipIf(platform.system() in ['Linux', ], "It crashes on Linux")
    def test_show(self):

        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

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


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppTabsInfoTab))
    return s
