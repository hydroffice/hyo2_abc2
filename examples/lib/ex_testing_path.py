import logging
from pathlib import Path

from hyo2.abc2.lib.testing_paths import TestingPaths
from hyo2.abc2.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

tp = TestingPaths(root_folder=Path(__file__).parent.parent.parent.resolve())

logger.debug("root folder: %s" % tp.root_folder)
logger.debug("root data folder: %s" % tp.root_data_folder())
logger.debug("input test files: %s" % tp.input_test_files(ext=""))  # "" for files without extension
