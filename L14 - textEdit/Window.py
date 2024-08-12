from PySide6 import QtWidgets
from PySide6.QtCore import QSize

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #main Widget
        self.mainWidget = MainWidget()
        #configs da janela
        self.setWindowTitle("janela")
        self.setCentralWidget(self.mainWidget)
        self.setWindowTitle("janela")

class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #widgets
        self.copyBtn = QtWidgets.QPushButton("copiar")
        self.cutBtn = QtWidgets.QPushButton("cortar")
        self.pasteBtn = QtWidgets.QPushButton("colar")
        self.undoBtn = QtWidgets.QPushButton("desfazer")
        self.redoBtn = QtWidgets.QPushButton("refazer")
        self.plainTxtBtn = QtWidgets.QPushButton("texto plano")
        self.htmlBtn = QtWidgets.QPushButton("html")
        self.clearBtn = QtWidgets.QPushButton("limpar")
        
        self.textEdit = QtWidgets.QTextEdit()

        #layout
        mainLayout = QtWidgets.QVBoxLayout()
        hLayout = QtWidgets.QHBoxLayout()

        #btns
        hLayout.addWidget(self.copyBtn)
        hLayout.addWidget(self.cutBtn)
        hLayout.addWidget(self.pasteBtn)
        hLayout.addWidget(self.undoBtn)
        hLayout.addWidget(self.redoBtn)
        hLayout.addWidget(self.plainTxtBtn)
        hLayout.addWidget(self.htmlBtn)
        hLayout.addWidget(self.clearBtn)
        
        mainLayout.addLayout(hLayout)
        mainLayout.addWidget(self.textEdit)

        #eventos
        self.copyBtn.clicked.connect(self.textEdit.copy)
        self.cutBtn.clicked.connect(self.textEdit.cut)
        self.pasteBtn.clicked.connect(self.textEdit.paste)
        self.undoBtn.clicked.connect(self.textEdit.undo)
        self.redoBtn.clicked.connect(self.textEdit.redo)
        self.plainTxtBtn.clicked.connect(self.set_plain_text)
        self.htmlBtn.clicked.connect(self.set_html)
        self.clearBtn.clicked.connect(self.textEdit.clear)

        #configs do widget
        self.setLayout(mainLayout)
    #funcs
    def set_plain_text(self):
        self.textEdit.setPlainText(self.textEdit.toPlainText())
    def set_html(self):
        self.textEdit.setHtml(self.textEdit.toPlainText())
