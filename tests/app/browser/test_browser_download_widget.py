import unittest
import sys

from PySide6 import QtWidgets, QtWebEngineWidgets

from hyo2.abc2.app.browser.download_widget import DownloadWidget


class TestAppBrowserDownloadWidget(unittest.TestCase):
    @unittest.skipIf(sys.platform == "linux", "Skip QWebEngine on Linux")
    def test_download(self):

        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        def download_requested(item):
            item.accept()
            w = DownloadWidget(download_request=item)
            mw.statusBar().addWidget(w)

        mw = QtWidgets.QMainWindow()
        view = QtWebEngineWidgets.QWebEngineView()
        # noinspection PyUnresolvedReferences
        view.page().profile().downloadRequested.connect(download_requested)
        mw.setCentralWidget(view)
        mw.show()

        view.page().download("https://www.hydroffice.org/static/mycommon/img/logo.png")


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppBrowserDownloadWidget))
    return s
