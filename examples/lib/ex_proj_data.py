import logging
import os

from hyo2.abc2.lib.gdal_aux import GdalAux
from hyo2.abc2.lib.logging import set_logging

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

GdalAux.check_proj4_data(verbose=True)
env_vars = ('PROJ_DATA', 'PROJ_LIB')
for env_var in env_vars:
    if env_var in os.environ:
        logger.debug('%s: %s' % (env_var, os.environ[env_var]))
GdalAux.check_proj4_data(verbose=True)
