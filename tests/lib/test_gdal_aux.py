import unittest
from pathlib import Path

from hyo2.abc2.lib.gdal_aux import GdalAux
from hyo2.abc2.lib.testing_paths import TestingPaths
from osgeo import ogr


class TestABCLibHelper(unittest.TestCase):

    def setUp(self):
        self.tp = TestingPaths(root_folder=Path(__file__).parent.parent.parent.resolve())

    def test_gdal_version(self):
        GdalAux.current_gdal_version()

    def test_create_ogr_data_source(self):
        for ogr_format in GdalAux.ogr_formats.keys():
            output_file = self.tp.output_data_folder().joinpath("ex_gdal_aux%s" % GdalAux.ogr_exts[ogr_format])
            if output_file.exists():
                output_file.unlink()

            output_ds = GdalAux.create_ogr_data_source(ogr_format=GdalAux.ogr_formats[ogr_format],
                                                       output_path=str(output_file))
            lyr = output_ds.CreateLayer("test", None, ogr.wkbPoint)
            self.assertIsNotNone(lyr)
            output_ds = None

    def test_gdal_data(self):
        GdalAux.check_gdal_data()

    def test_crs_id(self):
        wkt = """
        GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.01745329251994328,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]]
        """
        self.assertEqual(GdalAux.crs_id(wkt=wkt), "4326")


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibHelper))
    return s
