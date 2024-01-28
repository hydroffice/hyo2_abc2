import unittest

from PySide6 import QtWidgets

from hyo2.abc2.app.pkg_info import app_info
from hyo2.abc2.app.pkg_info.pkg_about.pkg_about_dialog import PkgAboutDialog
from hyo2.abc2.app.pkg_info.pkg_about.tabs.gdal_info_tab import GdalInfoTab
from hyo2.abc2.app.pkg_info.pkg_about.tabs.general_info_tab import GeneralInfoTab
from hyo2.abc2.app.pkg_info.pkg_about.tabs.license_tab import LicenseTab
from hyo2.abc2.app.pkg_info.pkg_about.tabs.local_environment_tab import LocalEnvironmentTab


class TestAppPkgAboutDialog(unittest.TestCase):

    def test_visibility(self):

        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        d = PkgAboutDialog(app_info=app_info)
        d.show()
        d.switch_visible()
        d.switch_visible()

    def test_with_all_tabs(self):

        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        d = PkgAboutDialog(app_info=app_info, with_gdal_tab=True, with_locale_tab=True)
        d.show()


class TestAppPkgAboutDialogGeneralInfoTab(unittest.TestCase):

    def test_visibility(self):
        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        t = GeneralInfoTab(app_info=app_info)
        t.show()


class TestAppPkgAboutDialogLicenseTab(unittest.TestCase):

    def test_visibility(self):
        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        t = LicenseTab(app_info=app_info)
        t.show()


class TestAppPkgAboutDialogLocalEnvironmentTab(unittest.TestCase):

    def test_visibility(self):
        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        t = LocalEnvironmentTab()
        t.show()


class TestAppPkgAboutDialogGdalInfoTab(unittest.TestCase):

    def test_visibility(self):
        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        t = GdalInfoTab()
        t.show()


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppPkgAboutDialog))
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppPkgAboutDialogGeneralInfoTab))
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppPkgAboutDialogLicenseTab))
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppPkgAboutDialogLocalEnvironmentTab))
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppPkgAboutDialogGdalInfoTab))
    return s
