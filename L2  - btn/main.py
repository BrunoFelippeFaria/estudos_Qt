import sys
from PySide6 import QtWidgets

def press():
    print("hello world!")

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow()
window.setWindowTitle("titulo")

btn = QtWidgets.QPushButton()
btn.setText("btn")

btn.clicked.connect(press)

window.setCentralWidget(btn)

window.show()
app.exec()
