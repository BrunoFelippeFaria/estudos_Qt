from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #sherek
        img = QtWidgets.QLabel()
        pixelmap = QPixmap("images/sherek.jpeg")
        img.setPixmap(QPixmap(pixelmap.scaled(700,500)))
        
        #configs da janela
        self.setWindowTitle("janela")
        self.setCentralWidget(img)
