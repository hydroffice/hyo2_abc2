import os
import unittest

from hyo2.abc2.lib.logging import set_logging
from hyo2.abc2.lib.testing import Testing
from hyo2.abc2.lib.ftp import Ftp

set_logging()


class TestABCLibFtp(unittest.TestCase):

    @unittest.skip("Temporarily disabling this test due to CCOM FTP")
    def test_init(self):
        _ = Ftp(host="ftp.ccom.unh.edu")

    @unittest.skip("Temporarily disabling this test due to CCOM FTP")
    def test_disconnect(self):
        ftp = Ftp(host="ftp.ccom.unh.edu", show_progress=False, debug_mode=False)
        ftp.disconnect()

    @unittest.skip("Temporarily disabling this test due to CCOM FTP")
    def test_download(self):
        root_folder = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
        tp = Testing(root_folder=root_folder)
        file_path = os.path.join(tp.output_data_folder(), "ccom.ico")

        if os.path.exists(file_path):
            os.remove(file_path)

        ftp = Ftp(host="ftp.ccom.unh.edu", password="test@gmail.com", show_progress=True, debug_mode=True)
        ftp.get_file(file_src="/it/files/images/ccom.ico", file_dst=file_path, unzip_it=False)
        ftp.disconnect()


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibFtp))
    return s
