from PySide6.QtWidgets import QApplication
import sys
from mainFrame import ventanaPrincipal

app = QApplication(sys.argv)
ventanaprincipal = ventanaPrincipal()
ventanaprincipal.show()
app.exec()