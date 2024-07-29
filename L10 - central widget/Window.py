from PySide6 import QtWidgets

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #itens
        btn = QtWidgets.QPushButton("me aperta!")
        btn2 = QtWidgets.QPushButton("aperta eu!")
        #layout
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(btn)
        layout.addWidget(btn2)
        #configs do widget
        self.setLayout(layout)
    



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #widget central
        self.Widget = Widget()
        self.setCentralWidget(self.Widget)        
        #configs da janela
        self.setWindowTitle("janela")
