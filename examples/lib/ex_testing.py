import logging
import os

from hyo2.abc2.lib.testing import Testing
from hyo2.abc2.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

t = Testing(root_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)))

logger.debug("root folder: %s" % t.root_folder)
logger.debug("root data folder: %s" % t.root_data_folder())
logger.debug("input test files: %s" % t.input_test_files(ext=""))  # "" for files without extension
