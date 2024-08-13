from PySide6 import QtWidgets

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #MainWidget
        self.mainWidget = MainWidget()
        #configs da janela
        self.setWindowTitle("janela")
        self.setCentralWidget(self.mainWidget)

class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #widgets 
        self.label = QtWidgets.QLabel("texto: ")
        self.lineEdit = QtWidgets.QLineEdit()
        self.btn1 = QtWidgets.QPushButton("um")
        self.btn2 = QtWidgets.QPushButton("dois")
        self.btn3 = QtWidgets.QPushButton("três")
        #configs dos widgets 
        
        self.lineEdit.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)


        #layout
        mainLayout = QtWidgets.QVBoxLayout()
        ln = QtWidgets.QHBoxLayout()
        ln2 = QtWidgets.QHBoxLayout()

        ln.addWidget(self.label)
        ln.addWidget(self.lineEdit)

        ln2.addWidget(self.btn1, stretch=2)
        ln2.addWidget(self.btn2, stretch=1)
        ln2.addWidget(self.btn3, stretch=1)

        mainLayout.addLayout(ln)
        mainLayout.addLayout(ln2)
        #configs da widget
        self.setLayout(mainLayout)


        
