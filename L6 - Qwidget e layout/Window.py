from PySide6 import QtWidgets

class Janela(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #atributos
        self.btn1 = QtWidgets.QPushButton("btn1")
        self.btn2 = QtWidgets.QPushButton("btn2")
        #configs do layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.btn2)
        #configs da janela
        self.setWindowTitle("janela")
        self.setLayout(self.layout)