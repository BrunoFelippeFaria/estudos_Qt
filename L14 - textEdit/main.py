import sys
from Window import Window
from PySide6.QtWidgets import QApplication

app = QApplication(sys.argv)
    
window = Window()
window.show()

app.exec()
