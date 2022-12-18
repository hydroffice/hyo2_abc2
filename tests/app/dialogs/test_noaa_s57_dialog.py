import os
import platform
import unittest

from PySide6 import QtWidgets

# import logging
# logging.basicConfig(level=logging.DEBUG)

from hyo2.abc2.app.dialogs.noaa_s57.noaa_s57 import NOAAS57Dialog
from hyo2.abc2.app.dialogs.noaa_s57.noaa_support import NOAASupport
from hyo2.abc2.lib.lib_info import LibInfo
from hyo2.abc2.app.app_info import AppInfo


class TestAppNOAAS57Dialog(unittest.TestCase):

    # @unittest.skipIf(platform.system() in ['Linux', ], "It crashes on Linux")
    def test_visibility(self):

        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        d = NOAAS57Dialog(lib_info=LibInfo(), app_info=AppInfo())
        d.show()

    def test_init(self):

        noaa_support = NOAASupport(lib_info=LibInfo(), app_info=AppInfo())

        self.assertTrue("v" in noaa_support.v_version())
        self.assertTrue(os.path.exists(noaa_support.internal_zip_path()))
        self.assertTrue(noaa_support.internal_zip_path_exists())


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppNOAAS57Dialog))
    return s
