from paginaPrincipal_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidgetItem, QMessageBox, QWidget,QDialog
from control_bd import BaseDatos 
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSizePolicy
from formularioControl import formularioAIControl, formularioDEControl, formularioREControl, formularioOrden, formularioAddPlato, formularioBorrarPlato, formularioEditPlato, busquedaEdicionPlato
from PySide6.QtGui import QColor, QPalette, QPainter
from exporControl import exportarControl
from datetime import datetime
import envios
import json


class paginaPrincipal(QMainWindow, Ui_MainWindow):  

    def __init__(self):
        super().__init__()

        self.caja = True
        self.setupUi(self)
        self.setWindowTitle("Chido TIF")
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.solo_iconos_widget.setHidden(True)
        self.Dashboard_boton_exp.clicked.connect(self.mostrar_dashboard)
        self.DashBoard_boton_s.clicked.connect(self.mostrar_dashboard)

        self.Inventario_boton_exp.clicked.connect(self.mostrar_inventario)
        self.Inventario_boton_s.clicked.connect(self.mostrar_inventario)

        self.Exportar_boton_exp.clicked.connect(self.mostrar_exportar)
        self.Exportar_boton_s.clicked.connect(self.mostrar_exportar)

        self.Ajustes_boton_exp.clicked.connect(self.mostrar_ajustes)
        self.Ajustes_boton_s.clicked.connect(self.mostrar_ajustes)

    

        self.mostrar_dashboard()
        self.crearTablaOrdenes()
        self.cargar_estado()
        self.listaReceta.hide()
        self.tablaPlatosInv.hide()
        self.labelInvenDis_2.hide()
        # Logica para buscar
        self.lineEdit.hide()
        self.pushButton_15.hide()
        self.pushButton_15.clicked.connect(self.buscarEnBase)

        # Logica Boton Actualizar
        self.actualizarBoton.clicked.connect(self.refrescarTabla)
        self.actualizarBoton.clicked.connect(self.crearTablaPlatosInv)

        # Logica conector inventario
        self.addInventarioBoton.clicked.connect(self.formularioAddInv)
        self.borrarInventarioBoton.clicked.connect(self.formularioBorrarInv)
        self.editarInventarioBoton.clicked.connect(self.formularioEditarInv)
        self.botonTogglePlatos.clicked.connect(self.togglePlatosInventario)
        self.tablaPlatosInv.cellDoubleClicked.connect(self.verReceta)

        # Logica conector ordenes
        self.genCompra.clicked.connect(self.formularioOrden)
        self.retirarOrden.clicked.connect(self.eliminarOrden)

        # Logica exportar 
        self.botonGenInv.clicked.connect(self.exportarInv)
        self.botonGenVentas.clicked.connect(self.exportarVen) 

        # Conectores ventas
        self.tablaOrdenes.cellDoubleClicked.connect(self.verOrden)
        self.genVal.clicked.connect(self.validarOrden)

        # Conectores ajustes
        self.botonStatusCaja.clicked.connect(self.cambiar_estado)
        self.botonAgregarPlatos.clicked.connect(self.formularioAddPlato)
        self.botonStatusCaja_2.clicked.connect(self.editarPlatos)
        self.botonStatusCaja_3.clicked.connect(self.borrarPlatos)
        self.botonStatusCaja_4.clicked.connect(self.enviarCorreoRegistros)

    def mostrar_dashboard(self):
        self.stackedWidget.setCurrentIndex(0)
        self.crearTablaOrdenes()
        self.actualizarBoton.show()
        self.lineEditNOrden.setStyleSheet("color:Black;")

    def mostrar_inventario(self):
        self.stackedWidget.setCurrentIndex(1)
        self.crearTablaInv()

    def mostrar_exportar(self):
        self.stackedWidget.setCurrentIndex(2)

    def mostrar_ajustes(self):
        self.stackedWidget.setCurrentIndex(3)

    def refrescarTabla(self):
        if self.stackedWidget.currentIndex() == 1:
            self.crearTablaInv()
        if self.stackedWidget.currentIndex() == 0:
            self.crearTablaOrdenes()
            self.ordenInfoTabla.clear()
            self.lineEditNOrden.clear()

    def cambiar_estado(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText('¿Estas seguro de realizar esta accion?\n'
                       'Se generara registro de la accion')
        msgBox.setWindowTitle('Confirmacion')
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        
        resultado = msgBox.exec_()
        if resultado == QMessageBox.Yes:
            self.caja = not self.caja 
            self.guardar_estado()  
            self.actualizarEstado()  
        else:
            msgBox = QMessageBox()
            msgBox.setText("Se cancelo la operacion")
            msgBox.setWindowTitle('Aviso')
            msgBox.exec_()
        
    def actualizarEstado(self):
        if not self.caja:
            self.pushButton.setStyleSheet(u"background-color: red;\n"
                                          "border-radius: 10px;\n"
                                          "border: 1px solid;")
            self.botonStatusCaja.setText("Abrir caja")
        else:
            self.pushButton.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
                                          "border-radius: 10px;\n"
                                          "border: 1px solid;")
            self.botonStatusCaja.setText("Cerrar caja")

    def guardar_estado(self):
        with open('estado.json', 'w') as file:
            json.dump({'caja': self.caja}, file)
        horaActual = datetime.now()
        fecha = horaActual.strftime("%Y-%m-%d")
        hora = horaActual.strftime("%H:%M")
        if not self.caja:
            BaseDatos.guardarEdicion([fecha, hora, "Se cerro la caja"])
        else: 
            BaseDatos.guardarEdicion([fecha, hora, "Se abrio la caja"])

    def cargar_estado(self):
        try:
            with open('estado.json', 'r') as file:
                data = json.load(file)
                self.caja = data.get('caja', False)
                self.actualizarEstado() 
        except FileNotFoundError:
            pass 

    def crearTablaInv(self):
        bd = BaseDatos.leerFilas()
        self.tableWidget.setRowCount(len(bd))
        self.lineEdit_2.setText(BaseDatos.ultimaEd())
        for _, fila in enumerate(bd):
            for __, elemento in enumerate(fila):
                item = QTableWidgetItem(str(elemento))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                item.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(_, __, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                color: black; /* Color del texto */
            }
            QTableWidget::item:selected {
                color: black; 
            }
            QTableWidget::item {
                border: 1px solid black; /* Borde de todas las celdas */
            }
            QHeaderView::section {
                color: black; /* Color del texto de la cabecera */
                font-weight: bold; /* Fuente en negrita */
            }
        """)

    def crearTablaPlatosInv(self):
        bd = BaseDatos.leerPlatos()
        self.tablaPlatosInv.setRowCount(len(bd))
        self.lineEdit_2.setText(BaseDatos.ultimaEd())
        for _, fila in enumerate(bd):
            for __, elemento in enumerate(fila):
                item = QTableWidgetItem(str(elemento))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                item.setTextAlignment(Qt.AlignCenter)
                self.tablaPlatosInv.setItem(_, __, item)
        self.tablaPlatosInv.verticalHeader().setVisible(False)
        self.tablaPlatosInv.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tablaPlatosInv.setStyleSheet("""
             QTableWidget {
                color: black; /* Color del texto */
            }
            QTableWidget::item:selected {
                background-color: rgb(94, 172, 36); /* Color de fondo de la celda seleccionada */
            }
            QTableWidget::item {
                border: 1px solid black; /* Borde de todas las celdas */
            }
            QHeaderView::section {
                color: black; /* Color del texto de la cabecera */
                font-weight: bold; /* Fuente en negrita */
            }
        """)

    def togglePlatosInventario(self):
        if self.labelInvenDis.text() == "Inventario Disponible":
            self.labelInvenDis.setText("Lista de platos")
            self.botonTogglePlatos.setText("Ver Inventario")
            self.borrarInventarioBoton.hide()
            self.editarInventarioBoton.hide()
            self.addInventarioBoton.hide()
            self.tableWidget.hide()

            self.listaReceta.show()
            self.listaReceta.clear()
            self.tablaPlatosInv.show()
            self.labelInvenDis_2.show()
            self.crearTablaPlatosInv()
        else:
            self.labelInvenDis.setText("Inventario Disponible")
            self.botonTogglePlatos.setText("Ver Platos Disponibles")
            self.borrarInventarioBoton.show()
            self.editarInventarioBoton.show()
            self.addInventarioBoton.show()
            self.tableWidget.show()

            self.listaReceta.hide()
            self.tablaPlatosInv.hide()
            self.labelInvenDis_2.hide()
            self.crearTablaInv()

    def verReceta(self):
        self.listaReceta.clear()
        seleccion = self.tablaPlatosInv.selectedItems()
        valores = BaseDatos.obtenerReceta(seleccion[0].text())
        for _ in valores:
            nombre = _[0]
            cantidad = _[1]
            unidad = _[2]
            self.listaReceta.addItem(f"{nombre}------{cantidad}-----{unidad}")

    def buscarEnBase(self):
        if self.tableWidget.isHidden():
            self.buscarEnPlat()
        else:
            self.buscarEnInv()

    def buscarEnPlat(self):
        self.tablaPlatosInv.clearContents()
        texto = self.lineEdit.text()
        bd = BaseDatos.buscarEnPlatos(texto)
        self.tablaPlatosInv.setRowCount(len(bd))
        for _, fila in enumerate(bd):
            for __, elemento in enumerate(fila):
                item = QTableWidgetItem(str(elemento))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.tablaPlatosInv.setItem(_, __, item)

    def buscarEnInv(self):
        self.tableWidget.clearContents()
        texto = self.lineEdit.text()
        bd = BaseDatos.buscarEnBd(texto)
        self.tableWidget.setRowCount(len(bd))
        for _, fila in enumerate(bd):
            for __, elemento in enumerate(fila):
                item = QTableWidgetItem(str(elemento))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.tableWidget.setItem(_, __, item)

    def formularioAddInv(self):
        _ = formularioAIControl()
        _.generarFormulario()
        if _.editado:
            horaActual = datetime.now()
            fecha = horaActual.strftime("%Y-%m-%d")
            hora = horaActual.strftime("%H:%M")
            BaseDatos.guardarEdicion([fecha, hora, f"Se agrego el articulo {_.LineEditNombreAI.text()}"])

    def formularioBorrarInv(self):
        _ = formularioDEControl()
        _.generarFormulario()
        if _.editado:
            horaActual = datetime.now()
            fecha = horaActual.strftime("%Y-%m-%d")
            hora = horaActual.strftime("%H:%M")
            BaseDatos.guardarEdicion([fecha, hora, f"Se borro el articulo {_.LineEditBuscarDE.text()}"])

    def formularioEditarInv(self):
        _ = formularioREControl()
        _.generarFormulario()
        if _.editado:
            horaActual = datetime.now()
            fecha = horaActual.strftime("%Y-%m-%d")
            hora = horaActual.strftime("%H:%M")
            BaseDatos.guardarEdicion([fecha, hora, f"Se ha añadido stock a '{_.edicionNomb}' por cantidad de '{_.edicionCan}'"])

    def crearTablaOrdenes(self):
        bd = BaseDatos.leerOrdenes()
        self.tablaOrdenes.setRowCount(len(bd))
        for _, fila in enumerate(bd):
            for __, elemento in enumerate(fila):
                item = QTableWidgetItem(str(elemento))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                item.setTextAlignment(Qt.AlignCenter)
                self.tablaOrdenes.setItem(_, __, item)
        self.tablaOrdenes.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tablaOrdenes.verticalHeader().setVisible(False)
        self.tablaOrdenes.setStyleSheet("""
            QTableWidget {
                color: black; /* Color del texto */
            }
            QTableWidget::item:selected {
                background-color: rgb(94, 172, 36); /* Color de fondo de la celda seleccionada */
            }
            QTableWidget::item {
                border: 1px solid black; /* Borde de todas las celdas */
            }
            QHeaderView::section {
                color: black; /* Color del texto de la cabecera */
                font-weight: bold; /* Fuente en negrita */
            }
        """)

    def verOrden(self):
        self.ordenInfoTabla.clear()
        seleccion = self.tablaOrdenes.selectedItems()
        valores = BaseDatos.datosOrden(seleccion[0].text())
        total = 0
        for _ in valores:
            nombre = _[1]
            precio = _[2]
            total += float(precio)
            self.ordenInfoTabla.addItem(f"{nombre} ------ {precio}")
        self.ordenInfoTabla.addItem(f"TOTAL A PAGAR ------ {total}")
        self.lineEditNOrden.setText(seleccion[0].text())

    def validarOrden(self):
        if not self.caja:
            self.mostrar_mensaje_error("La caja no está abierta. No se puede validar la orden.")
            return
        seleccion = self.tablaOrdenes.selectedItems()
        aviso = QMessageBox()
        color_texto = QColor(0, 0, 0) 
        palette = aviso.palette()
        palette.setColor(QPalette.Text, color_texto)
        aviso.setPalette(palette)
        if seleccion:
            if seleccion[2].text() == "N/A":
                horaActual = datetime.now()
                hora = horaActual.strftime("%H:%M")
                BaseDatos.actualizarVal(seleccion[0].text(), hora)
                aviso.setWindowTitle("Aviso")
                aviso.setText("Se validó la orden con éxito")
                aviso.exec()
                self.refrescarTabla()
            else:
                aviso.setWindowTitle("Aviso")
                aviso.setText("La orden ya se ha validado antes")
                aviso.exec()
        else:
            aviso.setWindowTitle("Aviso")
            aviso.setText("Debes seleccionar una orden para validar")
            aviso.exec()

    def eliminarOrden(self):
        if not self.caja:
            self.mostrar_mensaje_error("La caja no está abierta. No se puede eliminar la orden.")
            return
        seleccion = self.tablaOrdenes.selectedItems()
        aviso = QMessageBox()
        color_texto = QColor(0, 0, 0) 
        palette = aviso.palette()
        palette.setColor(QPalette.Text, color_texto)
        aviso.setPalette(palette)
        if seleccion:
            horaActual = datetime.now()
            hora = horaActual.strftime("%H:%M")
            BaseDatos.borrarOrden(int(seleccion[0].text()))
            fecha = horaActual.strftime("%Y-%m-%d")
            BaseDatos.guardarEdicion((fecha, hora, "Se borró una orden"))
            aviso.setWindowTitle("Aviso")
            aviso.setText("Se borró con éxito la orden")
            aviso.exec()
            self.refrescarTabla()
        else:
            aviso.setWindowTitle("Aviso")
            aviso.setText("Debes seleccionar una orden para eliminar")
            aviso.exec()

    def formularioOrden(self):
        if not self.caja:
            self.mostrar_mensaje_error("La caja no está abierta. No se puede generar una orden.")
            return
        _ = formularioOrden()
        _.generarFormulario()
        self.refrescarTabla()

    def formularioAddPlato(self):
        _ = formularioAddPlato()
        _.generarFormulario()

    def exportarInv(self):
        _ = exportarControl()
        _.exportarInventario()

    def exportarVen(self):
        _ = exportarControl()
        _.exportarVentas()

    def mostrar_mensaje_error(self, mensaje):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(mensaje)
        msgBox.setWindowTitle('Error')
        msgBox.exec_()

    def editarPlatos(self):
        dialogoBusqueda = busquedaEdicionPlato()
        dialogoBusqueda.exec_()
        if dialogoBusqueda.aceptado == True:
            platoSeleccionado = dialogoBusqueda.plato_seleccionado
            if platoSeleccionado:
                formularioEdicion = formularioEditPlato()
                formularioEdicion.generarFormulario(platoSeleccionado[0])


    def borrarPlatos(self):
        _ = formularioBorrarPlato()
        _.generarFormulario()
    

    def enviarCorreoRegistros(self):
        envios.enviar_email_con_adjunto()
        QMessageBox.information(None, "Informacion", "Se envio con exito el archivo")
