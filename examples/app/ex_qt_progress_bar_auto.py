import time
import logging
from PySide6 import QtWidgets

from hyo2.abc2.app.qt_progress import QtProgress
from hyo2.abc2.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

app = QtWidgets.QApplication([])

widget = QtWidgets.QWidget()
widget.show()

progress = QtProgress(parent=widget)

progress.start(title='Test Bar', text='Doing stuff', has_abortion=True)

time.sleep(.1)

for _ in range(10000):
    if progress.canceled:
        break
    progress.auto()
    time.sleep(.001)

print(f"canceled? {progress.canceled} (@{progress.value:.3f}%)")

progress.end()
