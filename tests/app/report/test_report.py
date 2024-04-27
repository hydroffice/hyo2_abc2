import os
import unittest
import sys

from PySide6 import QtWidgets

from hyo2.abc2.app.report.report import Report
from hyo2.abc2.lib.testing import Testing


class TestABCLibReport(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        root_folder = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir)
        cls.testing = Testing(root_folder=root_folder)

    @unittest.skipIf(sys.platform == "linux", "Skip PySide6 on Linux")
    def test_init(self):

        # noinspection PyArgumentList
        if not QtWidgets.QApplication.instance():
            QtWidgets.QApplication([])

        rep = Report(lib_name="TestReport", lib_version="1.0.0")

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

        rep.generate_pdf(path=os.path.join(self.testing.output_data_folder(), 'test.pdf'),
                         title="Test Document", use_colors=True, small=True)


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibReport))
    return s
