import os
import sys
import logging
from pathlib import Path

from PySide6 import QtWidgets

from hyo2.abc2.app.report import Report
from hyo2.abc2.lib.lib_info import LibInfo
from hyo2.abc2.lib.logging import set_logging
from hyo2.abc2.lib.testing_paths import TestingPaths

logger = logging.getLogger(__name__)
set_logging(ns_list=["hyo2.abc2"])

app = QtWidgets.QApplication([])

li = LibInfo()
r = Report(lib_name=li.lib_name, lib_version=li.lib_version)

t = TestingPaths(root_folder=Path(__file__).parent.parent.parent.resolve())
output_pdf = os.path.join(t.output_data_folder(), "%s.pdf" % os.path.splitext(os.path.basename(__file__))[0])
if os.path.exists(output_pdf):
    os.remove(output_pdf)
logger.debug('output pdf: %s' % output_pdf)

r += "Section 1 [SECTION]"

r += "Check 1 [CHECK]"
r += "OK"

r += "Check 2 [CHECK]"
r += "An issue"

r += "Section 2 [SKIP_SEC]"

r += "Check 3 [SKIP_CHK]"
r += "An issue"

r += "Total [TOTAL]"
r += "Issues: 3"
r += "Issues: 3 [SKIP_REP]"

r.generate_pdf(path=output_pdf, title="Test Report", use_colors=True)

# sys.exit(app.exec_())
