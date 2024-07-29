from PySide6 import QtWidgets
from PySide6.QtCore import QSize

class Janela(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        #status bar
        self.setStatusBar(QtWidgets.QStatusBar(self))

        #btn
        self.btn = QtWidgets.QPushButton("aperta!")
        self.btn.clicked.connect(self.press)

        #configs da janela
        self.setWindowTitle("janela")
        self.setFixedSize(QSize(700, 500))
        self.setCentralWidget(self.btn)


    def press(self):
        self.statusBar().showMessage("batata")
        self.statusBar().clearMessage()