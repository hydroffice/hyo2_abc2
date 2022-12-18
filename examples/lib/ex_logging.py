from hyo2.abc2.lib.logging import set_logging
import logging

ns_list = ["hyo2.test", ]
set_logging(ns_list=ns_list)

logger = logging.getLogger(__name__)

logger.debug("test debug")
logger.info("test info")
logger.warning("test warning")
logger.critical("test critical")
logger.error("test error")
