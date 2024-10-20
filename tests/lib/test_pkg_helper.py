import os
import unittest

from hyo2.abc2 import pkg_info
from hyo2.abc2.lib.package.pkg_helper import PkgHelper


class TestABCLibPkgHelper(unittest.TestCase):

    def setUp(self):

        self.h = PkgHelper(pkg_info=pkg_info)

    @unittest.skipIf(PkgHelper.is_linux(), "test not supported on Linux")
    def test_explore_folder(self):
        self.assertTrue(self.h.explore_folder(__file__))
        self.assertFalse(self.h.explore_folder(__file__ + ".fake"))
        self.assertTrue(self.h.explore_folder(os.path.dirname(__file__)))
        self.assertFalse(self.h.explore_folder(os.path.dirname(__file__) + "fake"))

    def test_first_match(self):
        # fake dict
        a_dict = {
            "a": 1,
            "b": 99,
            "c": 1,
        }

        # test if it gives back the first matching key
        self.assertTrue(PkgHelper.first_match(a_dict, 1) in ["a", "c"])

        # test if it raises with a not-existing value
        with self.assertRaises(RuntimeError):
            PkgHelper.first_match(a_dict, 2)

    def test_hstb_folders(self):
        if PkgHelper.is_pydro():
            self.assertTrue(os.path.exists(PkgHelper.hstb_folder()))
            self.assertTrue(os.path.exists(PkgHelper.hstb_atlases_folder()))
            self.assertTrue(os.path.exists(PkgHelper.hstb_woa09_folder()))
            self.assertTrue(os.path.exists(PkgHelper.hstb_woa13_folder()))
            self.assertTrue(os.path.exists(PkgHelper.hstb_woa18_folder()))

        else:
            self.assertRaises(RuntimeError, PkgHelper.hstb_folder)
            self.assertRaises(RuntimeError, PkgHelper.hstb_atlases_folder)
            self.assertRaises(RuntimeError, PkgHelper.hstb_woa09_folder)
            self.assertRaises(RuntimeError, PkgHelper.hstb_woa13_folder)
            self.assertRaises(RuntimeError, PkgHelper.hstb_woa18_folder)

    def test_is_64bit_os(self):
        self.assertIsInstance(self.h.is_64bit_os(), bool)

    def test_is_64bit_python(self):
        self.assertIsInstance(self.h.is_64bit_python(), bool)

    def test_is_darwin_linux_windows(self):
        self.assertIsInstance(self.h.is_darwin(), bool)
        self.assertIsInstance(self.h.is_linux(), bool)
        self.assertIsInstance(self.h.is_windows(), bool)

        self.assertTrue(any([self.h.is_linux(), self.h.is_darwin(), self.h.is_windows()]))

    def test_is_pydro(self):
        self.assertIsInstance(self.h.is_pydro(), bool)

    def test_is_url(self):
        self.assertTrue(self.h.is_url("https://www.hydroffice.org"))
        self.assertTrue(self.h.is_url("http://www.hydroffice.org"))
        self.assertFalse(self.h.is_url("ftp://fake/url"))

    def test_python_path(self):
        self.assertTrue(os.path.exists(self.h.python_path()))

    def test_package_info(self):
        self.assertIsInstance(self.h.pkg_info(qt_html=True), str)
        self.assertIsInstance(self.h.pkg_info(qt_html=False), str)

    def test_package_folder(self):
        self.assertTrue(os.path.exists(self.h.pkg_folder()))

    def test_hydroffice_folder(self):
        self.assertTrue(os.path.exists(self.h.hydroffice_folder()))

    def test_is_script_already_running(self):
        self.assertFalse(self.h.is_script_already_running())


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibPkgHelper))
    return s
