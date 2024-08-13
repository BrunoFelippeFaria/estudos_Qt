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
        #btns
        self.btn1 = QtWidgets.QPushButton("um")
        self.btn2 = QtWidgets.QPushButton("dois")
        self.btn3 = QtWidgets.QPushButton("três")
        self.btn4 = QtWidgets.QPushButton("quatro")
        self.btn5 = QtWidgets.QPushButton("cinco")
        self.btn6 = QtWidgets.QPushButton("seis")
        self.btn7 = QtWidgets.QPushButton("sete")
        
        self.btn3.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        
        #layout
        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.btn1, 0, 0)
        layout.addWidget(self.btn2, 0, 1, 1, 2)
        layout.addWidget(self.btn3, 1, 0, 2, 1)
        layout.addWidget(self.btn4, 1, 1)
        layout.addWidget(self.btn5, 1, 2)
        layout.addWidget(self.btn6, 2, 1)
        layout.addWidget(self.btn7, 2, 2)
        #configs do widget
        self.setLayout(layout)


