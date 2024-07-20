import sys
from PySide6.QtWidgets import QApplication
from Window import janela

app = QApplication(sys.argv)

window = janela()
window.show()

app.exec()