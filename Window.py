from PySide6 import QtWidgets

class janela(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #atributos
        self.btn = QtWidgets.QPushButton("aperte!")
        #configs da janela
        self.setWindowTitle("janela")
        self.setCentralWidget(btn)
        #configs dos widgets
        self.btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("hello world")
        