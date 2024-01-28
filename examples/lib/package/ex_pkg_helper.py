import logging
import os

from hyo2.abc2 import name
from hyo2.abc2 import __version__
from hyo2.abc2 import __file__ as abc2_file
from hyo2.abc2.lib.package.pkg_helper import PkgHelper
from hyo2.abc2.lib.package.pkg_info import PkgInfo
from hyo2.abc2.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])


pi = PkgInfo(
    name=name,
    version=__version__,
    author="G.Masetti (CCOM/JHC)",
    author_email="gmasetti@ccom.unh.edu",
    lic="LGPL v3",
    lic_url="https://www.hydroffice.org/license/",
    path=os.path.abspath(os.path.dirname(abc2_file)),
    url="https://www.hydroffice.org/abc/",
    manual_url="https://www.hydroffice.org/manuals/abc2/index.html",
    support_email="info@hydroffice.org",
    latest_url="https://www.hydroffice.org/latest/abc.txt",
    deps_dict={
            "gdal": "osgeo",
            "numpy": "numpy",
            "PySide6": "PySide6"
        }
)

ph = PkgHelper(pkg_info=pi)
logger.debug("lib info:\n%s" % ph.pkg_info())

logger.debug("is Pydro: %s" % PkgHelper.is_pydro())
if PkgHelper.is_pydro():
    logger.debug("HSTB folder: %s" % PkgHelper.hstb_folder())
    logger.debug("atlases folder: %s" % PkgHelper.hstb_atlases_folder())
    logger.debug("WOA09 folder: %s" % PkgHelper.hstb_woa09_folder())
    logger.debug("WOA13 folder: %s" % PkgHelper.hstb_woa13_folder())

app_info = pi.app_info(app_name="Test")
logger.debug("app name: %s" % app_info.app_name)
logger.debug("app version: %s" % app_info.app_version)

logger.info(app_info)
