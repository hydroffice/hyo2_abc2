from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
import sys


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt Web Browser")

        self.browser = QWebEngineView()
        # self.browser.setUrl("chrome://gpu/")
        self.browser.setUrl("https://get.webgl.org/")

        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec())
