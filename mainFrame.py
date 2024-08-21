from PySide6.QtWidgets import QMainWindow, QWidget, QApplication
import sys

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self._setUI()

    def _setUI(self):
        self.setGeometry(100,100,250,250)
        self.setWindowTitle("Aplicativo Chido")
        self.show()

