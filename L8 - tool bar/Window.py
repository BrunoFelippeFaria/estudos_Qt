from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QSize

class Janela(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #menu bar
        menuBar = self.menuBar()
        file_menu = menuBar.addMenu("&File")

        fechar = file_menu.addAction("Fechar")
        fechar.triggered.connect(self.fecharAction )

        edit_menu = menuBar.addMenu("&Editar")
        edit_menu.addAction("Selecionar")
        edit_menu.addAction("Copiar")
        edit_menu.addAction("Cortar")
        edit_menu.addAction("Colar")

 
        janela_menu = menuBar.addMenu("&Janela")
        config_menu = menuBar.addMenu("&configurações")
        ajuda_menu = menuBar.addMenu("&Ajuda")

        #tool bar
        toolBar = QtWidgets.QToolBar()
        action_tool = toolBar.addAction("action")
        action_tool.setToolTip("não faz nada")
        action_tool.triggered.connect(self.nada)

        #configs da janela
        self.setWindowTitle("janela")
        self.setMinimumSize(QSize(700,500))
        self.setMaximumSize(QSize(700,500))
        self.addToolBar(toolBar)


    def fecharAction(self):
        self.close()
    
    def nada(self):
        print("nada")