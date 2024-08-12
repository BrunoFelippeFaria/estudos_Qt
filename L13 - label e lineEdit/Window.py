from PySide6 import QtWidgets

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
        #widgets 
        self.label = QtWidgets.QLabel("nome: ")
        self.lineEdit = QtWidgets.QLineEdit()
        self.btn = QtWidgets.QPushButton("aperta!")

        #layout
        layout = QtWidgets.QVBoxLayout()
        layoutH = QtWidgets.QHBoxLayout()
        
        layoutH.addWidget(self.label)
        layoutH.addWidget(self.lineEdit)
        layout.addLayout(layoutH)
        layout.addWidget(self.btn)

        #eventos
        self.btn.clicked.connect(self.ola)
        
        #configs da QtWidget 
        self.setLayout(layout)

    
    def ola(self):
        msg = QtWidgets.QMessageBox.information(self, "olá", "olá " + self.lineEdit.text(), QtWidgets.QMessageBox.Ok)


