import sys
import logging

from PySide6 import QtWidgets, QtWebEngineWidgets
from hyo2.abc2.app.widgets.browser.download_widget import DownloadWidget
from hyo2.abc2.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])


def download_finished():
    logger.debug("finished")


def download_requested(item):
    item.accept()
    w = DownloadWidget(download_request=item)
    w.finished.connect(download_finished)
    mw.statusBar().addWidget(w)


app = QtWidgets.QApplication([])

mw = QtWidgets.QMainWindow()
view = QtWebEngineWidgets.QWebEngineView()
view.page().profile().downloadRequested.connect(download_requested)
mw.setCentralWidget(view)
mw.show()

view.page().download("https://www.hydroffice.org/static/app_root/img/logo.png")

sys.exit(app.exec())
