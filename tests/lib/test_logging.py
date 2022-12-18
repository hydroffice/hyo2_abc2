import logging
import unittest

from hyo2.abc2.lib.logging import set_logging


class TestABCLibLogging(unittest.TestCase):

    def setUp(self):
        set_logging(ns_list=["test_logging"])
        self.logger = logging.getLogger(__name__)

    def test_root_folder(self):
        self.logger.debug("test debug")
        self.logger.info("test info")
        self.logger.warning("test warning")
        self.logger.critical("test critical")
        self.logger.error("test error")


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibLogging))
    return s
