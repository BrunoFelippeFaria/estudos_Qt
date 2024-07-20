import sys
from PySide6.QtWidgets import QApplication
from Window import janela

def press(data):
    print(data)

app = QApplication(sys.argv) 
window = janela()
window.btn.clicked.connect(press)

window.show()
app.exec()
