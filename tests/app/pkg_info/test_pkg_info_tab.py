import unittest
import sys

from PySide6 import QtWidgets

from hyo2.abc2.app.pkg_info import app_info
from hyo2.abc2.app.pkg_info.pkg_info_tab import PkgInfoTab


class TestAppTabsPkgInfoTab(unittest.TestCase):

    @unittest.skipIf(sys.platform == "linux", "Skip PySide6 on Linux")
    def test_show(self):
        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        mw = QtWidgets.QMainWindow()

        t = PkgInfoTab(main_win=mw,
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


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppTabsPkgInfoTab))
    return s
