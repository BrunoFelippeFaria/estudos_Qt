import sys
from Window import janela
from PySide6.QtWidgets import QApplication

app = QApplication(sys.argv)

window = janela()
window.show()

app.exec()