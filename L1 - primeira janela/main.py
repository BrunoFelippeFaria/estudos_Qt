# Impotando os modulos

# o modulo sys é responsavel por processar argumentos de linha de comando 
import sys
# os modulos do pyside necessarios para iniciar uma janela
from PySide6.QtWidgets import QWidget, QApplication

app = QApplication(sys.argv)

window = QWidget()
window.show()
#inicia o loop de eventos
app.exec()