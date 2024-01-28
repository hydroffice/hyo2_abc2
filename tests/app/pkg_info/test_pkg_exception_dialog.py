import unittest

from PySide6 import QtWidgets

from hyo2.abc2.app.pkg_info import app_info
from hyo2.abc2.app.pkg_info.pkg_exception.pkg_exception_dialog import PkgExceptionDialog


class TestAppPkgExceptionDialog(unittest.TestCase):

    # @unittest.skipIf(platform.system() in ['Linux', ], "It crashes on Linux")
    def test_visibility(self):
        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        d = PkgExceptionDialog(app_info=app_info)
        d.show()


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAppPkgExceptionDialog))
    return s
