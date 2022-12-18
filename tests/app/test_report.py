from pathlib import Path
import platform
import unittest

from PySide6 import QtWidgets

from hyo2.abc2.app.report import Report
from hyo2.abc2.lib.lib_info import LibInfo
from hyo2.abc2.lib.testing_paths import TestingPaths


class TestABCLibReport(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.testing = TestingPaths(root_folder=Path(__file__).parent.parent.parent.resolve())

    # @unittest.skipIf(platform.system() in ['Linux', ], "It crashes on Linux")
    def test_init(self):

        # noinspection PyArgumentList
        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        li = LibInfo()
        rep = Report(lib_name=li.lib_name, lib_version=li.lib_version)

        rep += "Test [CHECK]"
        rep += "OK"

        rep += "Test [CHECK]"
        rep += "test"
        rep += "test"
        rep += "test"

        rep += "test [SKIP_CHK]"

        rep += "skip [SKIP_REP]"

        rep += "End [TOTAL]"
        rep += "Check 1 - Test"
        rep += "Check 2 - Test"

        rep.display()

        rep.generate_pdf(path=str(self.testing.output_data_folder().joinpath('test.pdf')),
                         title="Test Document", use_colors=True, small=True)


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibReport))
    return s
