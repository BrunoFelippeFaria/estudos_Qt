import sys
from PySide6 import QtWidgets

#classe da janela
class teste(QtWidgets.QMainWindow):
   def __init__(self):
        #inicia o construtor da classe QMainWindow
        super().__init__()
        #adiciona o btn como widget central
        self.setWindowTitle("teste")
        btn = QtWidgets.QPushButton("aperta")
        self.setCentralWidget(btn)


app = QtWidgets.QApplication(sys.argv)

window = teste()
window.show()

app.exec()
