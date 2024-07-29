import sys
from PySide6.QtWidgets import QApplication
from Window import Window

app = QApplication(sys.argv)

window = Window()
window.show()

app.exec()