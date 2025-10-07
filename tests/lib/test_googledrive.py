import os
import unittest

from hyo2.abc2.lib.testing import Testing
from hyo2.abc2.lib.googledrive import GoogleDrive


class TestABCGoogleDrive(unittest.TestCase):

    def test_init(self):
        _ = GoogleDrive()

    def test_download_and_unzip(self):
        googledrive_link = r"https://drive.google.com/file/d/1BbZ_CNnoAufpd9etw1crckA0Fe1yf3tx/view?usp=sharing"

        root_folder = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
        tp = Testing(root_folder=root_folder)
        zip_path = os.path.join(tp.output_data_folder(), "test.zip")
        unzip_path = os.path.join(tp.output_data_folder(), "test.txt")

        if os.path.exists(zip_path):
            os.remove(zip_path)
        if os.path.exists(unzip_path):
            os.remove(unzip_path)

        gd = GoogleDrive(show_progress=True, debug_mode=True)
        gd.get_file(file_src=googledrive_link, file_dst=zip_path, unzip_it=True)

        if os.path.exists(unzip_path):
            with open(unzip_path) as fid:
                text = fid.read().strip()
                self.assertEqual(text, "test")


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCGoogleDrive))
    return s
