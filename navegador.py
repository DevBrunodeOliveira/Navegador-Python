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

        # Barra de Navegação
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # Voltar
        btn_voltar = QAction('<', self)
        btn_voltar.triggered.connect(self.browser.back)
        toolbar.addAction(btn_voltar)

        # Avançar
        btn_avancar = QAction('>', self)
        btn_avancar.triggered.connect(self.browser.forward)
        toolbar.addAction(btn_avancar)

        # Atualizar
        btn_att = QAction('att', self)
        btn_att.triggered.connect(self.browser.reload)
        toolbar.addAction(btn_att)

        #Url
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.url_reader)
        toolbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.url_update)

    def url_reader(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    
    def url_update(self, url):
        self.url_bar.setText(url.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Navegador Python')
window = MainWindow()
app.exec_()
