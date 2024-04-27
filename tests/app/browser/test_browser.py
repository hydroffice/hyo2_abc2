import unittest
import sys

from PySide6 import QtCore, QtWidgets, QtTest

from hyo2.abc2.app.browser.browser import Browser


class TestAppBrowserBrowser(unittest.TestCase):

    @unittest.skipIf(sys.platform == "linux", "Skip QWebEngine on Linux")
    def test_change_url(self):

        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        w = Browser()
        initial_url = w.url()
        self.assertGreater(len(initial_url), 0)

        new_url = "https://www.google.com/"
        w.change_url(new_url)
        self.assertEqual(new_url, w.url())

    @unittest.skipIf(sys.platform == "linux", "Skip QWebEngine on Linux")
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
        # noinspection PyTypeChecker
        QtTest.QTest.keyClicks(w.address_line_edit, new_url, QtCore.Qt.KeyboardModifier.NoModifier, 1)
        QtTest.QTest.keyClick(w.address_line_edit, QtCore.Qt.Key_Enter)
        self.assertEqual(new_url, w.url())


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppBrowserBrowser))
    return s
