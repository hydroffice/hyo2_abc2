import time
import unittest
import sys
from PySide6 import QtWidgets

from hyo2.abc2.app.qt_progress import QtProgress


class TestABCAppQtProgress(unittest.TestCase):

    @unittest.skipIf(sys.platform == "linux", "Skip PySide6 on Linux")
    def test_run(self):

        # noinspection PyArgumentList
        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        widget = QtWidgets.QWidget()
        widget.show()

        progress = QtProgress(widget)

        progress.start(title='Test Bar', text='Doing stuff', min_value=100, max_value=300, init_value=100)

        time.sleep(.1)

        progress.update(value=150, text='Updating')

        time.sleep(.1)

        progress.add(quantum=50, text='Updating')

        time.sleep(.1)

        print("canceled? %s" % progress.canceled)

        progress.end()


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCAppQtProgress))
    return s
