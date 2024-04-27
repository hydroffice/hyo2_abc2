import os
import unittest
import sys

from PySide6 import QtWidgets

from hyo2.abc2.app.noaa_support.noaa_s57_dialog import NOAAS57Dialog
from hyo2.abc2.app.noaa_support.noaa_support import NOAASupport
from hyo2.abc2.app.pkg_info import app_info


class TestAppNOAAS57Dialog(unittest.TestCase):

    @unittest.skipIf(sys.platform == "linux", "Skip PySide6 on Linux")
    def test_visibility(self):
        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        d = NOAAS57Dialog(app_info=app_info)
        d.show()

    def test_init(self):
        noaa_support = NOAASupport(app_info=app_info)

        self.assertTrue("v" in noaa_support.v_version())
        self.assertTrue(os.path.exists(noaa_support.internal_zip_path()))
        self.assertTrue(noaa_support.internal_zip_path_exists())


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppNOAAS57Dialog))
    return s
