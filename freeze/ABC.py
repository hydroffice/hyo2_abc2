import sys
from PySide6 import QtWidgets, QtGui, QtCore

from hyo2.abc2.lib.helper import Helper
from hyo2.abc2.lib.lib_info import LibInfo
from hyo2.abc2.app.app_style import AppStyle
from hyo2.abc2.app.app_info import AppInfo
from hyo2.abc2.app.tabs.info.info_tab import InfoTab
from hyo2.abc2.lib.logging import set_logging


set_logging(ns_list=["hyo2.abc2", ])

sys.argv.append("--disable-web-security")  # temporary fix for CORS warning (QTBUG-70228)

app_info = AppInfo()
lib_info = LibInfo()

app = QtWidgets.QApplication([])
app.setApplicationName('%s' % app_info.app_name)
app.setOrganizationName("HydrOffice")
app.setOrganizationDomain("hydroffice.org")
app.setStyleSheet(AppStyle.load_stylesheet())

if Helper.is_script_already_running():
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

tabs = QtWidgets.QTabWidget()
mw.setCentralWidget(tabs)

t = InfoTab(app_info=app_info, lib_info=lib_info,
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


tabs.insertTab(0, t, "Info")

mw.show()

# print("browser storage: %s" % t.browser.view.page().profile().persistentStoragePath())

sys.exit(app.exec())
