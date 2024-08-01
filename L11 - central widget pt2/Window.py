from PySide6 import QtWidgets, QtCore

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #wiget
        appWiget = app()
        #menu bar
        menuBar = self.menuBar()
        menuApp = menuBar.addAction("&App")
        menuConfig = menuBar.addAction("&Configs")
        #actions
        menuApp.triggered.connect(self.changeApp)
        menuConfig.triggered.connect(self.changeConfig)

        #configs da janela
        self.setFixedSize(QtCore.QSize(900,500))
        self.setWindowTitle("janela")
        self.setCentralWidget(appWiget)
    #funçoes
    def changeApp(self):
        appWidget = app()
        self.setCentralWidget(appWidget)
    def changeConfig(self):
        confgWidget = config()
        self.setCentralWidget(confgWidget)

class app(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #label
        label = QtWidgets.QLabel("APP")
        #layout
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

class config(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #label
        label = QtWidgets.QLabel("config")
        #layout
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)