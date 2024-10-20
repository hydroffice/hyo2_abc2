import logging

from osgeo import gdal

from hyo2.abc2.lib.gdal_aux import GdalAux
from hyo2.abc2.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

GdalAux.check_gdal_data(verbose=True)
logger.debug('GDAL_DATA: %s' % gdal.GetConfigOption('GDAL_DATA'))
GdalAux.check_gdal_data(verbose=True)
