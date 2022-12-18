import unittest

from hyo2.abc2.lib.lib_info import LibInfo


class TestABCLibLibInfo(unittest.TestCase):

    def setUp(self):

        self.li = LibInfo()

    def test_is_string_type(self):
        self.assertIsInstance(self.li.lib_name, str)
        self.assertIsInstance(self.li.lib_version, str)
        self.assertIsInstance(self.li.lib_author, str)
        self.assertIsInstance(self.li.lib_author_email, str)

        self.assertIsInstance(self.li.lib_license, str)
        self.assertIsInstance(self.li.lib_license_url, str)

        self.assertIsInstance(self.li.lib_path, str)

        self.assertIsInstance(self.li.lib_url, str)
        self.assertIsInstance(self.li.lib_manual_url, str)
        self.assertIsInstance(self.li.lib_support_email, str)
        self.assertIsInstance(self.li.lib_latest_url, str)
        
    def test_no_empty_type(self):
        self.assertGreater(len(self.li.lib_name), 0)
        self.assertGreater(len(self.li.lib_version), 0)
        self.assertGreater(len(self.li.lib_author), 0)
        self.assertGreater(len(self.li.lib_author_email), 0)

        self.assertGreater(len(self.li.lib_license), 0)
        self.assertGreater(len(self.li.lib_license_url), 0)

        self.assertGreater(len(self.li.lib_path), 0)

        self.assertGreater(len(self.li.lib_url), 0)
        self.assertGreater(len(self.li.lib_manual_url), 0)
        self.assertGreater(len(self.li.lib_support_email), 0)
        self.assertGreater(len(self.li.lib_latest_url), 0)


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibLibInfo))
    return s
