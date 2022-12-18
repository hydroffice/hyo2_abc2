import logging

from hyo2.abc2.lib.helper import Helper
from hyo2.abc2.lib.lib_info import LibInfo
from hyo2.abc2.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

h = Helper(lib_info=LibInfo())

logger.debug("lib info:\n%s" % h.package_info())

logger.debug("is Pydro: %s" % Helper.is_pydro())

if Helper.is_pydro():
    logger.debug("HSTB folder: %s" % Helper.hstb_folder())
    logger.debug("atlases folder: %s" % Helper.hstb_atlases_folder())
    logger.debug("WOA09 folder: %s" % Helper.hstb_woa09_folder())
    logger.debug("WOA13 folder: %s" % Helper.hstb_woa13_folder())
