import platform
import unittest

from PySide6 import QtWidgets

# import logging
# logging.basicConfig(level=logging.DEBUG)

from hyo2.abc2.app.dialogs.exception.exception_dialog import ExceptionDialog
from hyo2.abc2.lib.lib_info import LibInfo
from hyo2.abc2.app.app_info import AppInfo


class TestAppExceptionDialog(unittest.TestCase):

    # @unittest.skipIf(platform.system() in ['Linux', ], "It crashes on Linux")
    def test_visibility(self):

        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        d = ExceptionDialog(lib_info=LibInfo(), app_info=AppInfo())
        d.show()


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppExceptionDialog))
    return s
