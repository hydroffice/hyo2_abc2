import logging
import os
import sys

from PySide6 import QtWidgets, QtGui, QtCore

from hyo2.abc2.app.app_style.app_style import AppStyle
from hyo2.abc2.app.pkg_info import app_info
from hyo2.abc2.app.pkg_info.pkg_info_tab import PkgInfoTab
from hyo2.abc2.lib.logging import set_logging
from hyo2.abc2.lib.package.pkg_helper import PkgHelper

set_logging(ns_list=["hyo2.abc2", ])
logger = logging.getLogger(__name__)

app = QtWidgets.QApplication(sys.argv)
app.setApplicationName(app_info.app_name)
app.setOrganizationName("HydrOffice")
app.setOrganizationDomain("hydroffice.org")
AppStyle.apply(app=app)

if PkgHelper.is_script_already_running():
    txt = "The app is already running!"
    msg_box = QtWidgets.QMessageBox()
    msg_box.setWindowTitle("Multiple Instances of ABC")
    msg_box.setIconPixmap(QtGui.QPixmap(app_info.app_icon_path).scaled(QtCore.QSize(36, 36)))
    msg_box.setText('%s\n\nDo you want to continue? This might create issues.' % txt)
    msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    msg_box.setDefaultButton(QtWidgets.QMessageBox.No)
    reply = msg_box.exec_()
    if reply == QtWidgets.QMessageBox.No:
        sys.exit(app.exit())

mw = QtWidgets.QMainWindow()
mw.setObjectName(app_info.app_main_window_object_name)
mw.setWindowTitle('%s v.%s' % (app_info.app_name, app_info.app_version))
mw.setWindowIcon(QtGui.QIcon(app_info.app_icon_path))
if PkgHelper.is_windows():

    try:
        # This is needed to display the app icon on the taskbar on Windows 7
        import ctypes

        app_id = '%s v.%s' % (app_info.app_name, app_info.app_version)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

    except AttributeError as e:
        logger.debug("Unable to change app icon: %s" % e)

tabs = QtWidgets.QTabWidget()
tabs.setIconSize(QtCore.QSize(55, 55))
mw.setCentralWidget(tabs)

t = PkgInfoTab(
    app_info=app_info,
    with_online_manual=True,
    with_offline_manual=True,
    with_bug_report=True,
    with_hydroffice_link=True,
    with_ccom_link=True,
    with_noaa_link=True,
    with_unh_link=True,
    with_license=True,
    with_noaa_57=True,
    main_win=mw)

idx_info = tabs.insertTab(0, t, QtGui.QIcon(os.path.join(PkgInfoTab.media, 'info.png')), "")
tabs.setTabToolTip(idx_info, "Info")

mw.show()

# print("browser storage: %s" % t.browser.view.page().profile().persistentStoragePath())

sys.exit(app.exec())
