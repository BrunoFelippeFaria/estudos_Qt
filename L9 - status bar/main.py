import sys
from PySide6.QtWidgets import QApplication
from Window import Janela

app = QApplication(sys.argv)

window = Janela()
window.show()

app.exec()  