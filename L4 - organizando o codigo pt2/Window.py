from PySide6 import QtWidgets

class janela(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        #atributos
        self.btn = QtWidgets.QPushButton("aperte!")
        #configruações da janela
        self.setWindowTitle("janela")
        self.setCentralWidget(self.btn)
        #configurações dos widgets
        self.btn.setCheckable(True)

    
