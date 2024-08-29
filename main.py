from PySide6.QtWidgets import QApplication, QMainWindow
from paginaPrincipal import paginaPrincipal
import sys

app = QApplication(sys.argv)
ventanaPrincipal = paginaPrincipal()
ventanaPrincipal.show()
app.exec()