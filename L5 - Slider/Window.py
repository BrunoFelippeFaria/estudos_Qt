from PySide6 import QtWidgets
from PySide6.QtCore import Qt 

class janela(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #slider
        self.slider = QtWidgets.QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.slide_pos)
        #configs da janela
        self.setWindowTitle("janela")
        self.setCentralWidget(self.slider)

    def slide_pos(self, pos):
        print(f"posição do slider: {pos}")