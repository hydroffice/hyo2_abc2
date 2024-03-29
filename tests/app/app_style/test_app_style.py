import unittest

from hyo2.abc2.app.app_style.app_style import AppStyle


class TestABCLibAppStyle(unittest.TestCase):

    def test_html_css(self):
        css_str = AppStyle.html_css()
        self.assertIsInstance(css_str, str)
        self.assertGreater(len(css_str), 0)


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibAppStyle))
    return s
