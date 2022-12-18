import unittest

from hyo2.abc2.app.app_info import AppInfo


class TestABCLibAppInfo(unittest.TestCase):

    def setUp(self):

        self.ai = AppInfo()

    def test_is_string_type(self):
        self.assertIsInstance(self.ai.app_name, str)
        self.assertIsInstance(self.ai.app_version, str)
        self.assertIsInstance(self.ai.app_author, str)
        self.assertIsInstance(self.ai.app_author_email, str)

        self.assertIsInstance(self.ai.app_license, str)
        self.assertIsInstance(self.ai.app_license_url, str)

        self.assertIsInstance(self.ai.app_path, str)

        self.assertIsInstance(self.ai.app_url, str)
        self.assertIsInstance(self.ai.app_manual_url, str)
        self.assertIsInstance(self.ai.app_support_email, str)
        self.assertIsInstance(self.ai.app_latest_url, str)

        # additional AppInfo-specific variables

        self.assertIsInstance(self.ai.app_media_path, str)
        self.assertIsInstance(self.ai.app_main_window_object_name, str)
        self.assertIsInstance(self.ai.app_license_path, str)
        self.assertIsInstance(self.ai.app_icon_path, str)
        
    def test_no_empty_type(self):
        self.assertGreater(len(self.ai.app_name), 0)
        self.assertGreater(len(self.ai.app_version), 0)
        self.assertGreater(len(self.ai.app_author), 0)
        self.assertGreater(len(self.ai.app_author_email), 0)

        self.assertGreater(len(self.ai.app_license), 0)
        self.assertGreater(len(self.ai.app_license_url), 0)

        self.assertGreater(len(self.ai.app_path), 0)

        self.assertGreater(len(self.ai.app_url), 0)
        self.assertGreater(len(self.ai.app_manual_url), 0)
        self.assertGreater(len(self.ai.app_support_email), 0)
        self.assertGreater(len(self.ai.app_latest_url), 0)

        # additional AppInfo-specific variables

        self.assertGreater(len(self.ai.app_media_path), 0)
        self.assertGreater(len(self.ai.app_main_window_object_name), 0)
        self.assertGreater(len(self.ai.app_license_path), 0)
        self.assertGreater(len(self.ai.app_icon_path), 0)


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibAppInfo))
    return s
