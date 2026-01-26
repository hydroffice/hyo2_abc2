import os
import unittest

from hyo2.abc2.lib.testing import Testing


class TestABCLibTesting(unittest.TestCase):

    def setUp(self):

        self.t = Testing(
            root_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)))

    def test_init(self):
        _ = Testing()

    def test_root_folder(self):
        self.assertTrue(os.path.exists(self.t.root_folder))
        self.assertGreater(len(Testing.files(folder=self.t.root_folder, ext="")), 0)

    def test_root_data_folder(self):
        self.assertTrue(os.path.exists(self.t.root_data_folder()))

    def test_input_data(self):
        self.assertTrue(os.path.exists(self.t.input_data_folder()))
        self.assertGreater(len(self.t.input_test_files(ext="")), 0)
        self.assertGreaterEqual(len(self.t.input_data_sub_folders()), 0)

    def test_input_data_sub_folders(self):
        self.assertGreaterEqual(len(self.t.input_data_sub_folders()), 0)

    def test_download_data(self):
        self.assertTrue(os.path.exists(self.t.download_data_folder()))
        self.assertGreaterEqual(len(self.t.download_test_files(ext="")), 0)

    def test_temp_data(self):
        self.t.delete_temp_folder()
        self.assertTrue(os.path.exists(self.t.temp_data_folder()))
        self.assertEqual(len(self.t.temp_test_files(ext="")), 0)
        self.assertEqual(len(self.t.temp_data_sub_folders()), 0)

    def test_reset_temp_folder(self):
        self.t.reset_temp_folder()
        self.assertGreaterEqual(len(self.t.temp_test_files(ext="")), 1)
        self.assertGreaterEqual(len(self.t.temp_data_sub_folders()), 0)
        self.t.delete_temp_folder()

    def test_output_data(self):
        self.assertTrue(os.path.exists(self.t.output_data_folder()))
        self.assertGreaterEqual(len(self.t.output_test_files(ext="")), 0)


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibTesting))
    return s
