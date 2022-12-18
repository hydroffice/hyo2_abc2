import unittest
import platform

from PySide6 import QtWidgets

# import logging
# logging.basicConfig(level=logging.DEBUG)

from hyo2.abc2.app.dialogs.about.about_dialog import AboutDialog
from hyo2.abc2.app.dialogs.about.tabs.general_info import GeneralInfoTab
from hyo2.abc2.app.dialogs.about.tabs.license import LicenseTab
from hyo2.abc2.app.dialogs.about.tabs.local_environment import LocalEnvironmentTab
from hyo2.abc2.app.dialogs.about.tabs.gdal_info import GdalInfoTab
from hyo2.abc2.lib.lib_info import LibInfo
from hyo2.abc2.app.app_info import AppInfo


class TestAppAboutDialog(unittest.TestCase):

    # @unittest.skipIf(platform.system() in ['Linux', ], "It crashes on Linux")
    def test_visibility(self):

        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        d = AboutDialog(lib_info=LibInfo(), app_info=AppInfo())
        d.show()
        d.switch_visible()
        d.switch_visible()

    # @unittest.skipIf(platform.system() in ['Linux', ], "It crashes on Linux")
    def test_with_all_tabs(self):

        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        d = AboutDialog(lib_info=LibInfo(), app_info=AppInfo(),
                        with_gdal_tab=True, with_locale_tab=True)
        d.show()


class TestAppAboutDialogGeneralInfoTab(unittest.TestCase):

    # @unittest.skipIf(platform.system() in ['Linux', ], "It crashes on Linux")
    def test_visibility(self):

        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        t = GeneralInfoTab(lib_info=LibInfo())
        t.show()


class TestAppAboutDialogLicenseTab(unittest.TestCase):

    # @unittest.skipIf(platform.system() in ['Linux', ], "It crashes on Linux")
    def test_visibility(self):

        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        t = LicenseTab(app_info=AppInfo())
        t.show()


class TestAppAboutDialogLocalEnvironmentTab(unittest.TestCase):

    # @unittest.skipIf(platform.system() in ['Linux', ], "It crashes on Linux")
    def test_visibility(self):

        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        t = LocalEnvironmentTab()
        t.show()


class TestAppAboutDialogGdalInfoTab(unittest.TestCase):

    # @unittest.skipIf(platform.system() in ['Linux', ], "It crashes on Linux")
    def test_visibility(self):

        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        t = GdalInfoTab()
        t.show()


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppAboutDialog))
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppAboutDialogGeneralInfoTab))
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppAboutDialogLicenseTab))
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppAboutDialogLocalEnvironmentTab))
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppAboutDialogGdalInfoTab))
    return s
