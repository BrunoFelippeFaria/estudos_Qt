from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QSize


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWidget = MainWidget()
        #configs da janela
        self.setWindowTitle("janela")
        self.setCentralWidget(self.mainWidget) 

class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #btns
        self.btnMsg = QtWidgets.QPushButton("mensagem")
        self.btnCritical = QtWidgets.QPushButton("Critical")

        self.btnMsg.clicked.connect(self.press)
        self.btnCritical.clicked.connect(self.pressCritical)

        #layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.btnMsg)
        layout.addWidget(self.btnCritical)
        #configs da widget 
        self.setLayout(layout)

    #esse é o jeito dificil de fazer uma mensagemBox
    def press(self):
        msg = QtWidgets.QMessageBox()
        msg.setMinimumSize(300,200)
        msg.setWindowTitle("aviso")
        msg.setText("deu ruim!")
        msg.setInformativeText("banana")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        
        res = msg.exec()

        if res == QMessageBox.Ok:
            print("ok")
        else:
            print("cancel")
    
    def pressCritical(self):
        res = QMessageBox.critical(self, "titulo", "mensagem critica!", QMessageBox.Ok | QMessageBox.Cancel)
        if res == QMessageBox.Ok:
            print("ok")
        else:
            print("cancel")
        
    #além do QMessageBox.critical, tem o question, information, warning e o about

