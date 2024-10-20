import unittest

from hyo2.abc2.lib.ftp import Ftp


class TestABCLibFtp(unittest.TestCase):

    def test_init(self):
        ftp = Ftp(host="ftp.ccom.unh.edu", password="test@gmail.com", show_progress=True, debug_mode=True)
        ftp.disconnect()


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibFtp))
    return s
