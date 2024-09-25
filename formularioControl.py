from formularioAI_ui import Ui_DialogoAddInventario
from dialogoAgregarPlatos import Ui_AgregarPlato
from addPlatoAc_ui import Ui_ingredienteCan
from editarPlato_ui import Ui_ingredienteC
from dialogoEditarPlato import Ui_EditarPlato
from formBorrarInv_ui import Ui_BorrarInv
from formEditarInv_ui import Ui_EditarInv
from ui_borrarPlato import Ui_borrarPlato
from buscarParaEditar import Ui_busquedaEdicion
from dialogoOrden_ui import Ui_orden
from PySide6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QWidget, QListWidgetItem
from control_bd import BaseDatos
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSizePolicy

class formularioAIControl(QDialog,Ui_DialogoAddInventario):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.editado = False
        self.BotonesFormAI.accepted.connect(self.acep)
        self.BotonesFormAI.rejected.connect(self.reje)
        
    def generarFormulario(self):
        self.exec_()

    def acep(self):
        if BaseDatos.existeEnLaBase(self.LineEditNombreAI.text()):  
            QMessageBox.warning(self, "Error", "El objeto a añadir ya existe en la base de datos")  
        else:
            try:
                instruccion = []
                instruccion.append(self.LineEditNombreAI.text())
                instruccion.append(float(self.LineEditCantidadAI.text()))
                instruccion.append(self.lineEditUnidadDeMedidaAI.text())
                BaseDatos.insertarElemento(instruccion)
                QMessageBox.information(self,"Informacion", "La operacion se realizo con exito")
                self.editado = True
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Error al añadir objeto a la base de datos: {str(e)}")
    def reje(self):
        QMessageBox.information(self, "Informacion", "Se ha cancelado la operacion")
    
class formularioDEControl(QDialog,Ui_BorrarInv):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.editado = False
        self.buttonBox.accepted.connect(self.acep)
        self.buttonBox.rejected.connect(self.reje)
        self.buscarBotonDE.clicked.connect(self.busquedaDE)

    def generarFormulario(self):
        self.exec_()

    def busquedaDE(self):
         if not BaseDatos.existeEnLaBase(self.LineEditBuscarDE.text()):
             QMessageBox.warning(self, "Error", "El objeto a borrar no existe en la base de datos")
         else:
             valores = BaseDatos.buscarEnBdUnic(self.LineEditBuscarDE.text())
             self.LineEditDEnombre.setText(valores[0])
             self.LineEditCantidadDE.setText(str(valores[1]))
             self.lineEditUnidadDeMedidaDE.setText(valores[2])

    def acep(self):
       _ = QMessageBox()
       _.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
       _.setWindowTitle("Confirmar Operación")
       _.setText("¿Estás seguro de que quieres borrar el objeto seleccionado?")
       _.setIcon(QMessageBox.Question)
       _.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
       _.button(QMessageBox.Yes).setText('Confirmar')
       _.button(QMessageBox.No).setText('Cancelar')
       __ = _.exec_()
       if __ == QMessageBox.Yes:
            if self.LineEditDEnombre.text()=="":
                QMessageBox.warning(self, "Error", "Debes buscar el objeto a borrar")
            else: 
                try:
                    BaseDatos.borrarBd(self.LineEditDEnombre.text())
                    QMessageBox.information(self,"Informacion", "La operacion se realizo con exito")
                    self.editado = True
                except Exception as e:
                    QMessageBox.warning(self,"Informacion", "La operacion no pudo realizarse")
       else:
           self.reje()

    def reje(self):
        QMessageBox.information(self, "Informacion", "Se ha cancelado la operacion")

class formularioREControl(QDialog,Ui_EditarInv):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.editado = False
        self.edicionNomb = ""
        self.edicionCan = 0
        self.valorAnterior = 0
        self.buttonBox.accepted.connect(self.acep)
        self.buttonBox.rejected.connect(self.reje)
        self.buscarBotonRE.clicked.connect(self.busquedaRE)

    def generarFormulario(self):
        self.exec_()

    def busquedaRE(self):
         if not BaseDatos.existeEnLaBase(self.LineEditBuscarRE.text()):
             QMessageBox.warning(self, "Error", "El objeto a borrar no existe en la base de datos")
         else:
             valores = BaseDatos.buscarEnBdUnic(self.LineEditBuscarRE.text())
             self.lineEditUnidadDeMedidaRE.setText(valores[2])
             self.doubleSpinBoxRE.setValue(valores[1])
             self.valorAnterior = valores[1]

    def acep(self):
        try:
            val=[]

            val.append(self.LineEditBuscarRE.text())
            val.append(self.doubleSpinBoxRE.value())
            valorActual = val[1]
            BaseDatos.actualizarBd(val)
            QMessageBox.information(self,"Informacion", "Se completo la operacion con exito")
            self.editado = True
            self.edicionNomb = val[0]
            self.edicionCan = valorActual - self.valorAnterior
        except: 
            QMessageBox.warning(self,"Error", "Ocurrio un error")
    def reje(self):
        QMessageBox.information(self, "Informacion", "Se ha cancelado la operacion")

class formularioOrden(QDialog,Ui_orden):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tablaOrden.verticalHeader().setVisible(False)
        self.buttonBox.accepted.connect(self.acep)
        self.buttonBox.rejected.connect(self.reje)
        self.botonBusquedaOrdenRe.clicked.connect(self.busqedaPlatos)
        self.botonAgregarPlatoOrden.clicked.connect(self.agregarPlato)
        self.totalAPagar=0.0
        self.lineaPrecioOrdenRe.setText(str(0))
        self.pushButton.clicked.connect(self.retirarPlato)

        bd = BaseDatos.leerPlatos()
        self.tablaOrden.setRowCount(len(bd))
        for _, fila in enumerate(bd):
            for __, elemento in enumerate(fila):
                item = QTableWidgetItem(str(elemento))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.tablaOrden.setItem(_,__,item)
        self.tablaOrden.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


    def generarFormulario(self):
        self.exec_()

    def busqedaPlatos(self):
         self.tablaOrden.clearContents()
         texto = self.buscadorOrdenRe.text()
         bd = BaseDatos.buscarEnPlatos(texto)
         self.tablaOrden.setRowCount(len(bd))
         for _, fila in enumerate(bd):
             for __, elemento in enumerate(fila):
                 item = QTableWidgetItem(str(elemento))
                 item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                 self.tablaOrden.setItem(_,__,item)
         self.tablaOrden.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
         

    def agregarPlato(self):
        plato = self.tablaOrden.selectedItems()

        if plato:

            row = plato[0].row()
            nombre = self.tablaOrden.item(row,0).text()
            precio = self.tablaOrden.item(row,1).text()
            self.listOrden.addItem(f"{nombre} ------ {precio}")
            self.totalAPagar += float(precio)
            self.lineaPrecioOrdenRe.setText(str(self.totalAPagar))
            
        else: 
            QMessageBox.warning(self,"Error","Debes seleccionar un plato de la tabla")
        
    def retirarPlato(self):
        item = self.listOrden.currentItem()
        if item:
            _= item.text().split()
            self.totalAPagar-=float(_[2])
            self.lineaPrecioOrdenRe.setText(str(self.totalAPagar))
            self.listOrden.takeItem(self.listOrden.row(item))
        else:
             QMessageBox.warning(self,"Error","Debes seleccionar un plato de la lista de la orden")

    def acep(self):
        if self.listOrden.count() == 0:
            QMessageBox.information(self,"Informacion","La operacion se ha cancelado")
        else:
            lista = []
            for index in range(self.listOrden.count()):
                _ = self.listOrden.item(index).text().split()
                nombre = _[0]
                lista.append(nombre)
            BaseDatos.registrarVenta(lista)
            BaseDatos.registrarOrden(float(self.lineaPrecioOrdenRe.text()))
            QMessageBox.information(self,"Informacion","Se completo la operacion con exito")
    def reje(self):
        QMessageBox.information(self,"Informacion","La operacion se ha cancelado")

class formularioAddPlato(QDialog,Ui_AgregarPlato):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tablaIngredientes.verticalHeader().setVisible(False)
        self.buttonBox.accepted.connect(self.acep)
        self.buttonBox.rejected.connect(self.reje)
        self.botonBusquedaIngrediente.clicked.connect(self.buscarIngrediente)
        self.botonAgregarIngrediente.clicked.connect(self.agregarIngredientes)
        self.botonRetirarIngrediente.clicked.connect(self.retirarIngrediente)
        bd = BaseDatos.leerIngredientes()
        self.tablaIngredientes.setRowCount(len(bd))
        for _, fila in enumerate(bd):
            for __, elemento in enumerate(fila):
                item = QTableWidgetItem(str(elemento))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.tablaIngredientes.setItem(_,__,item)
        self.tablaIngredientes.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.form = QDialog()
        self.ui = Ui_ingredienteCan()
        self.ui.setupUi(self.form)
        self.ui.botonesAc.accepted.connect(self.acepac)
        self.ui.botonesAc.rejected.connect(self.rejecac)
        self.listaIngredientesTotal = {}
    
    def generarFormulario(self):
        self.exec_()

    def buscarIngrediente(self):
        self.tablaIngredientes.clearContents()
        texto = self.buscadorIngrediente.text()
        bd = BaseDatos.buscarIngredientes(texto)
        self.tablaIngredientes.setRowCount(len(bd))
        for _, fila in enumerate(bd):
            for __, elemento in enumerate(fila):
                item = QTableWidgetItem(str(elemento))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.tablaIngredientes.setItem(_,__,item)
        self.tablaIngredientes.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def agregarIngredientes(self):
        ingrediente = self.tablaIngredientes.selectedItems()

        if ingrediente:
            row = ingrediente[0].row()
            self.nombre = self.tablaIngredientes.item(row,0).text()
            self.medida = self.tablaIngredientes.item(row,1).text()
            self.ui.nombreIngredienteAc.setText(self.nombre)
            self.ui.medidaIngredienteAc.setText(self.medida)
            self.form.exec_()
        else: 
            QMessageBox.warning(self,"Error","Debes seleccionar un plato de la tabla")

    def retirarIngrediente(self):
        indice = self.listReceta.currentRow()
        if indice != -1:  
            item = self.listReceta.takeItem(indice)  
            if item:  
                QMessageBox.information(self, "Información", f"Ingrente '{item.text()}' retirado correctamente.")
        else:
            QMessageBox.warning(self, "Error", "Debes seleccionar un ingrediente de la receta.")


    def acepac(self):
        cantidad = self.ui.spinboxCantidad.value()
        self.listReceta.addItem(f"{self.nombre}------{cantidad}--{self.medida}")
        self.listaIngredientesTotal[self.nombre] = cantidad

    def rejecac(self):
        QMessageBox.information(self,"Informacion", "La operacion se ha cancelado")

    def acep(self):
        nombrePlato = self.nombrePlatoIngrediente.text()
        precioPlato = (self.precioPlatoIngrediente.text())
        if len(nombrePlato.split())!=1:
            QMessageBox.information(self,"Informacion","se debe usar _ en lugar de espacios")

        else:
            if nombrePlato!="" and precioPlato!="":
                BaseDatos.agregarPlatoConIngredientes(nombrePlato,float(precioPlato),self.listaIngredientesTotal)
                QMessageBox.information(self,"Informacion","Se completo la creacion")
    
    def reje(self):
        pass

class formularioBorrarPlato(QDialog,Ui_borrarPlato):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buscarBotonDE.clicked.connect(self.buscar)
        self.botonesBorrarPlato.accepted.connect(self.acep)
        self.botonesBorrarPlato.rejected.connect(self.reje)
    def acep(self):
        _ = BaseDatos.borrarPlato(self.LineEditBuscarDE.text())
        if _: 
            QMessageBox.information(self,"Informacion",f"Se borro {self.LineEditBuscarDE.text()} exitosamente")
        else:
            QMessageBox.information(self,"Informacion",f"El Plato '{self.LineEditBuscarDE.text()}' no existe en la base de datos")
    def reje(self):
        QMessageBox.information(self,"Informacion", "Se cancelo la operacion")

    def buscar(self):
        if BaseDatos.existeEnPlatos(self.LineEditBuscarDE.text()):
            self.listWidget.clear()
            valores = BaseDatos.obtenerReceta(self.LineEditBuscarDE.text())
            for _ in valores:
                nombre = _[0]
                cantidad = _[1]
                unidad = _[2]
                self.listWidget.addItem(f"{nombre}------{cantidad}-----{unidad}")
            QMessageBox.information(self,"Informacion","Se completo la busqueda")
        else:
            QMessageBox.information(self,"Informacion",f"El Plato '{self.LineEditBuscarDE.text()}' no existe en la base de datos")


    def generarFormulario(self):
        self.exec_()

class busquedaEdicionPlato(QDialog, Ui_busquedaEdicion):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.botonesBorrarPlato.accepted.connect(self.seleccionarPlato)
        self.buscarBotonDE.clicked.connect(self.buscarPlato)
        self.listWidget.itemDoubleClicked.connect(self.seleccionarPlato)
        self.platoSeleccionado = None
        self.aceptado = False

    def buscarPlato(self):
        # Obtener el nombre del plato que se busca
        nombre = self.LineEditBuscarDE.text().strip()

        if nombre:
            # Buscar en la base de datos platos que coincidan con el nombre
            resultados = BaseDatos.buscarEnPlatos(nombre)
            self.listWidget.clear()

            if resultados:
                # Asumimos que resultados es una lista de tuplas y tomamos el primer resultado
                # Puedes modificar esto según la lógica de tu aplicación
                self.plato_seleccionado = resultados[0]  # Seleccionamos el primer plato encontrado
                # Obtener la receta del plato seleccionado
                valores = BaseDatos.obtenerReceta(self.plato_seleccionado[0])  # Asumiendo que el nombre del plato es el primer elemento

                if valores:
                    for ingrediente, cantidad, unidad in valores:
                        self.listWidget.addItem(f"{ingrediente} ------ {cantidad} ----- {unidad}")
                else:
                    QMessageBox.information(self, "Sin ingredientes", f"No se encontraron ingredientes para el plato '{self.plato_seleccionado[0]}'")
            else:
                QMessageBox.warning(self, "Sin resultados", f"No se encontraron platos con el nombre '{nombre}'")
        
        self.LineEditBuscarDE.setText(self.plato_seleccionado[0])

    def seleccionarPlato(self):
        if self.plato_seleccionado:
            self.aceptado = True

    def obtenerPlatoSeleccionado(self):
        return self.platoSeleccionado

class formularioEditPlato(QDialog, Ui_EditarPlato):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tablaIngredientes.verticalHeader().setVisible(False)
        self.buttonBox.accepted.connect(self.acep)  # Conectar el botón de aceptar para editar el plato
        self.buttonBox.rejected.connect(self.reje)
        self.botonBusquedaIngrediente.clicked.connect(self.buscarIngrediente)
        self.botonAgregarIngrediente.clicked.connect(self.agregarIngredientes)
        self.botonRetirarIngrediente.clicked.connect(self.retirarIngrediente)
        # Inicializar variables de diálogo para agregar ingredientes
        self.form = QDialog()
        self.ui = Ui_ingredienteCan()
        self.ui.setupUi(self.form)
        self.ui.botonesAc.accepted.connect(self.acepac)
        self.ui.botonesAc.rejected.connect(self.rejecac)
        self.listaIngredientesTotal = {}

    def generarFormulario(self, nombre_plato):
        # Rellenar los datos del formulario con el plato a editar
        self.nombrePlatoIngrediente.setText(nombre_plato)
        self.nombreAEditar = nombre_plato
        plato_info = BaseDatos.buscarEnPlatos(nombre_plato)
        self.precioPlatoIngrediente.setText(str(plato_info[0][1]))
        ingredientes = BaseDatos.obtenerReceta(nombre_plato)
        bd = BaseDatos.leerIngredientes()
        self.listReceta.clear()
        self.tablaIngredientes.setRowCount(len(bd))
        for _, fila in enumerate(bd):
            for __, elemento in enumerate(fila):
                item = QTableWidgetItem(str(elemento))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.tablaIngredientes.setItem(_,__,item)
        self.tablaIngredientes.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.exec_()

    def buscarIngrediente(self):
        self.tablaIngredientes.clearContents()
        texto = self.buscadorIngrediente.text()
        bd = BaseDatos.buscarIngredientes(texto)
        self.tablaIngredientes.setRowCount(len(bd))
        for _, fila in enumerate(bd):
            for __, elemento in enumerate(fila):
                item = QTableWidgetItem(str(elemento))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.tablaIngredientes.setItem(_, __, item)
        self.tablaIngredientes.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def agregarIngredientes(self):
        ingrediente = self.tablaIngredientes.selectedItems()

        if ingrediente:
            row = ingrediente[0].row()
            self.nombre = self.tablaIngredientes.item(row, 0).text()
            self.medida = self.tablaIngredientes.item(row, 1).text()
            self.ui.nombreIngredienteAc.setText(self.nombre)
            self.ui.medidaIngredienteAc.setText(self.medida)
            self.form.exec_()
        else:
            QMessageBox.warning(self, "Error", "Debes seleccionar un ingrediente de la tabla")
    
    def retirarIngrediente(self):
        indice = self.listReceta.currentRow()
        if indice != -1:  
            item = self.listReceta.takeItem(indice)  
            if item:  
                QMessageBox.information(self, "Información", f"Ingrente '{item.text()}' retirado correctamente.")
        else:
            QMessageBox.warning(self, "Error", "Debes seleccionar un ingrediente de la receta.")

    def acepac(self):
        cantidad = self.ui.spinboxCantidad.value()
        self.listReceta.addItem(f"{self.nombre}------{cantidad}--{self.medida}")
        self.listaIngredientesTotal[self.nombre] = cantidad

    def rejecac(self):
        QMessageBox.information(self, "Informacion", "La operación se ha cancelado")

    def acep(self):
        nombrePlato = self.nombreAEditar
        nuevoNombrePlato = self.nombrePlatoIngrediente.text()
        precioPlato = self.precioPlatoIngrediente.text()
        
        if len(nombrePlato.split()) != 1:
            QMessageBox.information(self, "Informacion", "Se debe usar _ en lugar de espacios en el nombre del plato")
        else:
            if nombrePlato != "" and precioPlato != "":
                nuevo_nombre = nuevoNombrePlato if nuevoNombrePlato != "" else None
                nuevo_precio = float(precioPlato) if precioPlato != "" else None
                BaseDatos.editarPlato(nombrePlato, nuevo_nombre, nuevo_precio, self.listaIngredientesTotal)
                QMessageBox.information(self, "Informacion", "Se completó la edición del plato")
    
    def reje(self):
        pass
