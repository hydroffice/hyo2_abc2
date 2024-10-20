import os
import unittest

from hyo2.abc2.lib.gdal_aux import GdalAux
from hyo2.abc2.lib.testing import Testing
from osgeo import ogr


class TestABCLibHelper(unittest.TestCase):

    def setUp(self):
        root_folder = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
        self.tp = Testing(root_folder=root_folder)

    def test_gdal_version(self):
        vers = GdalAux.current_gdal_version()
        self.assertGreater(vers, 0)

    def test_create_ogr_data_source(self):
        for ogr_format in GdalAux.ogr_formats.keys():
            output_file = os.path.join(self.tp.output_data_folder(), "ex_gdal_aux%s" % GdalAux.ogr_exts[ogr_format])
            if os.path.exists(output_file):
                os.remove(output_file)

            output_ds = GdalAux.create_ogr_data_source(ogr_format=GdalAux.ogr_formats[ogr_format],
                                                       output_path=str(output_file))
            lyr = output_ds.CreateLayer("test", None, ogr.wkbPoint)
            self.assertIsNotNone(lyr)
            output_ds = None

    def test_list_ogr_drivers(self):
        GdalAux.list_ogr_drivers()

    def test_push_gdal_error_handler(self):
        GdalAux.push_gdal_error_handler()

    def test_gdal_data(self):
        GdalAux.check_gdal_data(verbose=True)

    def test_proj4_data(self):
        GdalAux.check_proj4_data(verbose=True)

    def test_lat_long_to_zone_number(self):
        zone = GdalAux.lat_long_to_zone_number(43.13555, -70.9395)
        self.assertEqual(zone, 19)

    def test_crs_id(self):
        wkt = """
        GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.01745329251994328,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]]
        """
        self.assertEqual(GdalAux.crs_id(wkt=wkt), "4326")


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibHelper))
    return s
