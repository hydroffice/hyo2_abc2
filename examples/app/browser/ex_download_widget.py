import logging
import sys

from PySide6 import QtWidgets, QtWebEngineWidgets

from hyo2.abc2.app.app_style.app_style import AppStyle
from hyo2.abc2.app.browser.download_widget import DownloadWidget
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


app = QtWidgets.QApplication(sys.argv)
AppStyle.apply(app)

mw = QtWidgets.QMainWindow()
view = QtWebEngineWidgets.QWebEngineView()
# noinspection PyUnresolvedReferences
view.page().profile().downloadRequested.connect(download_requested)
mw.setCentralWidget(view)
mw.show()

view.page().download("https://www.hydroffice.org/static/app_root/img/logo.png")

sys.exit(app.exec())
