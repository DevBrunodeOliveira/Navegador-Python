from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.tabs =QTabWidget()
        self.tabs.setDocumentMode(True)
        #self.tabs.tabBarDoubleClicked.connect(self.nova_aba)
        #self.tabs.currentChanged.connect(self.troca_de_aba)
        self.tabs.setTabsClosable(True)
        #self.tabs.tabCloseRequested.connect(self.fechar_aba)
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
        navbar.addAction(self.urlbar)

        self.add_aba(QUrl('http://www.google.com'))

        self.show()
        self.setWindowTitle("Python Navegador")

    


app = QApplication(sys.argv)
QApplication.setApplicationName('Navegador Python')
window = MainWindow()
app.exec_()
