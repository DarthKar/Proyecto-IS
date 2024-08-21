from PySide6.QtWidgets import QMainWindow
from ui_mainframe import Ui_mainframe
class ventanaPrincipal(QMainWindow,Ui_mainframe):
    
    def __init__(self):
        super().__init__()
        self.setupUi()

    
