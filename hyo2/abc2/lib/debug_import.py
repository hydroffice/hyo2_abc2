class DebugImport:

    def __init__(self, logging_name: str | None = None, numpy: bool = False, pyproj: bool = False, gdal: bool = False,
                 qt: bool = False, matplotlib: bool = False, cartopy: bool = False):
        import logging
        import time

        log_path = None
        if logging_name:
            import os
            home_folder = os.path.expanduser("~")
            log_folder = os.path.join(home_folder, f".{logging_name.lower()}")
            if not os.path.exists(log_folder):
                os.makedirs(log_folder)
            log_path = os.path.join(log_folder, time.strftime("%Y%m%d_%H%M%S.log"))

        from hyo2.abc2.lib.logging import set_logging
        set_logging(ns_list=[""], default_logging=logging.DEBUG, hyo2_logging=logging.DEBUG, lib_logging=logging.DEBUG,
                    file_logging=log_path)
        logger = logging.getLogger(__name__)
        logger.info(f"Logging to: {log_path}")
        logger.info("DEBUG IMPORT ...")

        if numpy:
            logger.debug("First numpy import ...")
            start = time.perf_counter()
            # noinspection PyUnresolvedReferences
            import numpy as np
            logger.debug("First numpy import ... DONE (%.3f s)" % (time.perf_counter() - start))

        if pyproj:
            logger.debug("First pyproj import ...")
            start = time.perf_counter()
            # noinspection PyUnresolvedReferences
            import pyproj as pj
            logger.debug("First pyproj import ... DONE (%.3f s)" % (time.perf_counter() - start))

        if gdal:
            logger.debug("First gdal, ogr, osr import ...")
            start = time.perf_counter()
            # noinspection PyUnresolvedReferences
            from osgeo import gdal as gd, ogr, osr
            logger.debug("First gdal, ogr, osr import ... DONE (%.3f s)" % (time.perf_counter() - start))

        if qt:
            logger.debug("First QtCore, QtWidgets, QtGui import ...")
            start = time.perf_counter()
            # noinspection PyUnresolvedReferences
            from PySide6 import QtCore, QtWidgets, QtGui
            logger.debug("First QtCore, QtWidgets, QtGui import ... DONE (%.3f s)" % (time.perf_counter() - start))

            logger.debug("First qt_material import ...")
            start = time.perf_counter()
            # noinspection PyUnresolvedReferences
            from qt_material import apply_stylesheet
            logger.debug("First qt_material import ... DONE (%.3f s)" % (time.perf_counter() - start))

        if matplotlib:
            logger.debug("First matplotlib import ...")
            start = time.perf_counter()
            # noinspection PyUnresolvedReferences
            from matplotlib import pyplot as plt
            logger.debug("First matplotlib import ... DONE (%.3f s)" % (time.perf_counter() - start))

        if cartopy:
            logger.debug("First cartopy import ...")
            start = time.perf_counter()
            # noinspection PyUnresolvedReferences
            import cartopy.crs as ccrs
            logger.debug("First cartopy import ... DONE (%.3f s)" % (time.perf_counter() - start))

        logger.info("DEBUG IMPORT ... DONE")
