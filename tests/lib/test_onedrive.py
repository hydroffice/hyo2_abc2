import os
import unittest

from hyo2.abc2.lib.testing import Testing
from hyo2.abc2.lib.onedrive import OneDrive


class TestABCOneDrive(unittest.TestCase):

    def test_init(self):
        _ = OneDrive()

    def test_download_and_unzip(self):
        onedrive_link = r"https://1drv.ms/u/c/3579835830bc10b0/EbODspITBp5Cu-OWyxXVaRkBzHMZFA8GsvCYOmQCUJfLzw?e=9auP6y"

        root_folder = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
        tp = Testing(root_folder=root_folder)
        zip_path = os.path.join(tp.output_data_folder(), "test.zip")
        unzip_path = os.path.join(tp.output_data_folder(), "test.txt")

        if os.path.exists(zip_path):
            os.remove(zip_path)
        if os.path.exists(unzip_path):
            os.remove(unzip_path)

        od = OneDrive(show_progress=True, debug_mode=True)
        od.get_file(file_src=onedrive_link, file_dst=zip_path, unzip_it=True)

        if os.path.exists(unzip_path):
            with open(unzip_path) as fid:
                text = fid.read().strip()
                self.assertEqual(text, "test")


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCOneDrive))
    return s
