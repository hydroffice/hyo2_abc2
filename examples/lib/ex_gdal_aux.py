import logging
import os.path
from osgeo import ogr

from hyo2.abc2.lib.testing import Testing
from hyo2.abc2.lib.gdal_aux import GdalAux
from hyo2.abc2.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

root_folder = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
tp = Testing(root_folder=root_folder)

gdal_version = GdalAux.current_gdal_version()
logger.debug("GDAL version: %s" % gdal_version)

for ogr_format in GdalAux.ogr_formats.keys():
    output_file = os.path.join(tp.output_data_folder(), "ex_gdal_aux%s" % GdalAux.ogr_exts[ogr_format])
    if os.path.exists(output_file):
        os.remove(output_file)
    logger.debug("file: %s" % output_file)

    output_ds = GdalAux.create_ogr_data_source(ogr_format=GdalAux.ogr_formats[ogr_format],
                                               output_path=str(output_file))
    lyr = output_ds.CreateLayer("test", None, ogr.wkbPoint)
    output_ds = None
