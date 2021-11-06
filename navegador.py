from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.tabs =QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.nova_aba)
        self.tabs.currentChanged.connect(self.troca_de_aba)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.fechar_aba)
        self.setCentralWidget(self.tabs)
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        navbar = QToolBar()
        self.addToolBar(navbar)

        voltar_btn = QAction("<", self)
        voltar_btn.setToolTip("Voltar")
        voltar_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        navbar.addAction(voltar_btn)

        avancar_btn = QAction(">", self)
        avancar_btn.setToolTip("Avançar")
        avancar_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navbar.addAction(avancar_btn)

        att_btn = QAction("R",self)
        att_btn.setToolTip("Atualizar")
        att_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navbar.addAction(att_btn)

        navbar.addSeparator()

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.nav_url)
        navbar.addWidget(self.urlbar)

        self.add_aba(QUrl('http://www.google.com'), "Nova Guia")

        self.show()
        self.setWindowTitle("Python Navegador")

    def add_aba(self, qurl=None, label="Blank"):

        if qurl == None:
            qurl = QUrl('http://www.google.com')
        navegador = QWebEngineView()
        navegador.setUrl(qurl)
        i = self.tabs.addTab(navegador, label)
        self.tabs.setCurrentIndex(i)
        #navegador.urlChanged.connect(lambda qurl, navegador = navegador: self.att_url(qurl, navegador))
        navegador.loadFinished.connect(lambda _, i = i, navegador = navegador: self.tabs.setTabText(i, navegador.page().title()))
    
    def nova_aba(self, i):
        if i == -1:
            self.add_aba()

    def troca_de_aba(self, i):
        qurl = self.tabs.currentWidget().url()
        self.att_urlbar(qurl, self.tabs.currentWidget())
        self.att_titulo(self.tabs.currentWidget())
    
    def fechar_aba(self, i):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(i)
    
    def att_titulo(self, navegador):
        if navegador != self.tabs.currentWidget():
            return
        titulo = self.tabs.currentWidget().page().title()
        self.setWindowTitle(f'{titulo}')

    def att_urlbar(self, url, navegador = None):
        if navegador != self.tabs.currentWidget():
            return
        self.urlbar.setText(url.toString())
        self.urlbar.setCursorPosition(0)

    def nav_url(self):
        url = QUrl(self.urlbar.text())
        if url.scheme == "":
            url.scheme('http')
        self.tabs.currentWidget().setUrl(url)
        pass

    


app = QApplication(sys.argv)
QApplication.setApplicationName('Navegador Python')
window = MainWindow()
app.exec_()
