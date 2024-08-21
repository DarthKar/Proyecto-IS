from PySide6.QtWidgets import QMainWindow, QWidget, QApplication
import sys

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self._setUI()

    def _setUI(self):
        self.resize(800,600)
        self.setWindowTitle("TIF")
        self.show()
