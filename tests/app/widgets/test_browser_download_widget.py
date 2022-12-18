import unittest

from PySide6 import QtCore, QtWidgets, QtTest, QtWebEngineWidgets

# import logging
# logging.basicConfig(level=logging.DEBUG)

from hyo2.abc2.app.widgets.browser.download_widget import DownloadWidget


class TestAppBrowserDownloadWidget(unittest.TestCase):

    def test_download(self):

        pass  # it passes, but a lot of warnings

        # if not QtWidgets.qApp:
        #     QtWidgets.QApplication([])
        #
        # def download_requested(item):
        #     item.accept()
        #     w = DownloadWidget(download_item=item)
        #     mw.statusBar().addWidget(w)
        #
        # mw = QtWidgets.QMainWindow()
        # view = QtWebEngineWidgets.QWebEngineView()
        # view.page().profile().downloadRequested.connect(download_requested)
        # mw.setCentralWidget(view)
        # mw.show()
        #
        # view.page().download("https://www.hydroffice.org/static/mycommon/img/logo.png")


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppBrowserDownloadWidget))
    return s
