import sys
import time
import unittest

from hyo2.abc2.lib.progress.cli_progress import CliProgress


class TestABCLibCliProgress(unittest.TestCase):

    def setUp(self):
        self.progress = CliProgress()

    def test_start_minimal(self):
        try:
            self.progress.start()
        except Exception as e:
            self.fail(e)

    def test_start_custom_title_text(self):
        try:
            self.progress.start(title='Test Bar', text='Doing stuff')
        except Exception as e:
            self.fail(e)

    def test_start_custom_min_max(self):
        try:
            self.progress.start(min_value=100, max_value=300, init_value=100)
        except Exception as e:
            self.fail(e)

    def test_start_minimal_update(self):
        try:
            self.progress.start()
            self.progress.update(50)
        except Exception as e:
            self.fail(e)

    def test_start_minimal_update_raising(self):
        with self.assertRaises(Exception) as context:
            self.progress.start()
            self.progress.update(1000)

    def test_start_minimal_add(self):
        try:
            self.progress.start()
            self.progress.add(50)
        except Exception as e:
            self.fail(e)

    def test_start_minimal_add_raising(self):
        with self.assertRaises(Exception) as context:
            self.progress.start()
            self.progress.add(1000)

    def test_auto(self):
        for _ in range(1000):
            self.progress.auto()
        self.progress.end()

    def test_run(self):
        progress = CliProgress()

        progress.start(title='Test Bar', text='Doing stuff', min_value=100, max_value=300, init_value=100)

        time.sleep(.1)

        progress.update(value=150, text='Updating')

        time.sleep(.1)

        progress.add(quantum=50, text='Updating')

        time.sleep(.1)

        self.assertFalse(progress.canceled)

        progress.end()


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibCliProgress))
    return s
