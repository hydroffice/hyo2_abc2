import sys
from PySide6 import QtCore, QtWidgets, QtWebEngineWidgets

app = QtWidgets.QApplication()
q = QtWebEngineWidgets.QWebEngineView()
q.load(QtCore.QUrl('https://www.google.com/'))
q.show()
sys.exit(app.exec())
