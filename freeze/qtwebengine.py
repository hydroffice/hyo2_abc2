import sys

from PySide6 import QtCore, QtWidgets, QtWebEngineWidgets

app = QtWidgets.QApplication(sys.argv)
qw = QtWebEngineWidgets.QWebEngineView()
qw.load(QtCore.QUrl('https://www.google.com/'))
qw.show()
sys.exit(app.exec())
