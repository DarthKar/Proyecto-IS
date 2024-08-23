from PySide6.QtWidgets import QMainWindow, QWidget, QApplication
from ui_mainframe import Ui_mainframe


class ventanaPrincipal(QMainWindow,Ui_mainframe):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.solo_iconos_widget.hide()
        self.Ordenes_boton_exp.clicked.connect(self.cambioOrdenes)
        self.Inventario_boton_exp.clicked.connect(self.cambioInventario)
    

    def cambioOrdenes(self):
        self.stackedWidget.setCurrentIndex(0)

    def cambioInventario(self):
        self.stackedWidget.setCurrentIndex(1) #cambio de pestañas 