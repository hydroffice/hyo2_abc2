import logging
from pathlib import Path
from osgeo import ogr

from hyo2.abc2.lib.testing_paths import TestingPaths
from hyo2.abc2.lib.gdal_aux import GdalAux
from hyo2.abc2.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

tp = TestingPaths(root_folder=Path(__file__).parent.parent.parent.resolve())

gdal_version = GdalAux.current_gdal_version()
logger.debug("GDAL version: %s" % gdal_version)

for ogr_format in GdalAux.ogr_formats.keys():
    output_file = tp.output_data_folder().joinpath("ex_gdal_aux%s" % GdalAux.ogr_exts[ogr_format])
    if output_file.exists():
        output_file.unlink()
    logger.debug("file: %s" % output_file)

    output_ds = GdalAux.create_ogr_data_source(ogr_format=GdalAux.ogr_formats[ogr_format],
                                               output_path=str(output_file))
    lyr = output_ds.CreateLayer("test", None, ogr.wkbPoint)
    output_ds = None
