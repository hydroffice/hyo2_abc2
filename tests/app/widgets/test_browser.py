import unittest
import platform

from PySide6 import QtCore, QtWidgets, QtTest

# import logging
# logging.basicConfig(level=logging.DEBUG)

from hyo2.abc2.app.widgets.browser.browser import Browser


class TestAppBrowserBrowser(unittest.TestCase):

    @unittest.skipIf(platform.system() in ['Darwin', 'Linux', 'Windows'], "Temporarily disabled")
    def test_change_url(self):

        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        w = Browser()
        initial_url = w.url()
        self.assertGreater(len(initial_url), 0)

        new_url = "https://www.google.com/"
        w.change_url(new_url)
        self.assertEqual(new_url, w.url())

    @unittest.skipIf(platform.system() in ['Darwin', 'Linux', 'Windows'], "Temporarily disabled")
    def test_type_url(self):

        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        w = Browser()
        initial_url = w.url()
        new_url = "https://www.google.com/"
        QtTest.QTest.keyClick(w.address_line_edit, QtCore.Qt.Key_Enter)

        # remove current characters
        for _ in initial_url:
            QtTest.QTest.keyClick(w.address_line_edit, QtCore.Qt.Key_Backspace)
        QtTest.QTest.keyClicks(w.address_line_edit, new_url, 0, 1)
        QtTest.QTest.keyClick(w.address_line_edit, QtCore.Qt.Key_Enter)
        self.assertEqual(new_url, w.url())


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppBrowserBrowser))
    return s
