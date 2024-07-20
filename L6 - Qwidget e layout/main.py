import sys
from PySide6.QtWidgets import QApplication
from Window import Janela

def btn1_clicked():
    print("botão 1")
def btn2_clicked():
    print("botão 2")


app = QApplication(sys.argv)
window = Janela()

window.btn1.clicked.connect(btn1_clicked)
window.btn2.clicked.connect(btn2_clicked)

window.show()
app.exec()