import sys
import logging

from PySide6 import QtWidgets
from hyo2.abc2.app.widgets.browser.browser import Browser
from hyo2.abc2.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

app = QtWidgets.QApplication([])

w = Browser()
w.show()

# w.change_url("https://www.google.com")
# logger.debug("current url: %s" % w.url())

sys.exit(app.exec())
