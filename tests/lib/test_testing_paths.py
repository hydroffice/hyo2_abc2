from pathlib import Path
import unittest

from hyo2.abc2.lib.testing_paths import TestingPaths


class TestABCLibTestingPaths(unittest.TestCase):

    def setUp(self):

        self.tp = TestingPaths(
            root_folder=Path(__file__).parent.parent.parent.resolve())

    def test_root_folder(self):
        self.assertTrue(self.tp.root_folder.exists())
        self.assertGreater(len(TestingPaths.files(folder=self.tp.root_folder, ext="")), 0)

    def test_input_data(self):
        self.assertTrue(self.tp.input_data_folder().exists())
        self.assertGreater(len(self.tp.input_test_files(ext="")), 0)
        self.assertGreaterEqual(len(self.tp.input_data_sub_folders()), 0)

    def test_download_data(self):
        self.assertTrue(self.tp.download_data_folder().exists())
        self.assertGreaterEqual(len(self.tp.download_test_files(ext="")), 0)

    def test_temp_data(self):
        self.assertTrue(self.tp.temp_data_folder().exists())
        self.assertGreaterEqual(len(self.tp.temp_test_files(ext="")), 0)

    def test_output_data(self):
        self.assertTrue(self.tp.output_data_folder().exists())
        self.assertGreaterEqual(len(self.tp.output_test_files(ext="")), 0)


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibTestingPaths))
    return s
