from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://github.com/DevBrunodeOliveira'))
        self.setCentralWidget(self.browser)
        self.showMaximized()


app = QApplication(sys.argv)
QApplication.setApplicationName('Navegador Python')
window = MainWindow()
app.exec_()
