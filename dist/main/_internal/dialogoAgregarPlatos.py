from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QFormLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_AgregarPlato(object):
    def setupUi(self, OrdenRequest):
        if not OrdenRequest.objectName():
            OrdenRequest.setObjectName(u"OrdenRequest")
        OrdenRequest.resize(633, 534)
        self.buttonBox = QDialogButtonBox(OrdenRequest)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(270, 490, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.labelReceta = QLabel(OrdenRequest)
        self.labelReceta.setObjectName(u"labelReceta")
        self.labelReceta.setGeometry(QRect(340, 150, 81, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.labelReceta.setFont(font)
        self.tablaIngredientes = QTableWidget(OrdenRequest)
        if (self.tablaIngredientes.columnCount() < 2):
            self.tablaIngredientes.setColumnCount(2)
        font1 = QFont()
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tablaIngredientes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tablaIngredientes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tablaIngredientes.setObjectName(u"tablaIngredientes")
        self.tablaIngredientes.setGeometry(QRect(10, 50, 301, 411))
        self.tablaIngredientes.setMinimumSize(QSize(281, 411))
        self.tablaIngredientes.setDragDropMode(QAbstractItemView.InternalMove)
        self.tablaIngredientes.setGridStyle(Qt.CustomDashLine)
        self.tablaIngredientes.horizontalHeader().setDefaultSectionSize(150)
        self.tablaIngredientes.horizontalHeader().setStretchLastSection(False)
        self.tablaIngredientes.verticalHeader().setCascadingSectionResizes(False)
        self.tablaIngredientes.verticalHeader().setDefaultSectionSize(32)
        self.layoutWidget = QWidget(OrdenRequest)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 321, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.buscadorIngrediente = QLineEdit(self.layoutWidget)
        self.buscadorIngrediente.setObjectName(u"buscadorIngrediente")
        self.buscadorIngrediente.setFont(font1)

        self.horizontalLayout_2.addWidget(self.buscadorIngrediente)

        self.botonBusquedaIngrediente = QPushButton(self.layoutWidget)
        self.botonBusquedaIngrediente.setObjectName(u"botonBusquedaIngrediente")
        self.botonBusquedaIngrediente.setFont(font1)

        self.horizontalLayout_2.addWidget(self.botonBusquedaIngrediente)

        self.layoutWidget1 = QWidget(OrdenRequest)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(130, 470, 158, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.botonAgregarIngrediente = QPushButton(self.layoutWidget1)
        self.botonAgregarIngrediente.setObjectName(u"botonAgregarIngrediente")
        self.botonAgregarIngrediente.setFont(font1)

        self.horizontalLayout_3.addWidget(self.botonAgregarIngrediente)

        self.botonRetirarIngrediente = QPushButton(self.layoutWidget1)
        self.botonRetirarIngrediente.setObjectName(u"botonRetirarIngrediente")
        self.botonRetirarIngrediente.setFont(font1)

        self.horizontalLayout_3.addWidget(self.botonRetirarIngrediente)

        self.listReceta = QListWidget(OrdenRequest)
        self.listReceta.setObjectName(u"listReceta")
        self.listReceta.setGeometry(QRect(335, 171, 271, 261))
        self.layoutWidget2 = QWidget(OrdenRequest)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(340, 80, 271, 72))
        self.formLayout = QFormLayout(self.layoutWidget2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget2)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.nombrePlatoIngrediente = QLineEdit(self.layoutWidget2)
        self.nombrePlatoIngrediente.setObjectName(u"nombrePlatoIngrediente")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nombrePlatoIngrediente)

        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.precioPlatoIngrediente = QLineEdit(self.layoutWidget2)
        self.precioPlatoIngrediente.setObjectName(u"precioPlatoIngrediente")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.precioPlatoIngrediente)

        self.label_2 = QLabel(OrdenRequest)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 40, 281, 31))
        self.label_2.setFont(font1)

        self.retranslateUi(OrdenRequest)
        self.buttonBox.accepted.connect(OrdenRequest.accept)
        self.buttonBox.rejected.connect(OrdenRequest.reject)

        QMetaObject.connectSlotsByName(OrdenRequest)
    # setupUi

    def retranslateUi(self, OrdenRequest):
        OrdenRequest.setWindowTitle(QCoreApplication.translate("OrdenRequest", u"Dialog", None))
        self.labelReceta.setText(QCoreApplication.translate("OrdenRequest", u"Receta", None))
        ___qtablewidgetitem = self.tablaIngredientes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("OrdenRequest", u"Nombre", None));
        ___qtablewidgetitem1 = self.tablaIngredientes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("OrdenRequest", u"Und. de medida", None));
        self.buscadorIngrediente.setText("")
        self.buscadorIngrediente.setPlaceholderText(QCoreApplication.translate("OrdenRequest", u"Escribe aqui el nombre del ingrediente", None))
        self.botonBusquedaIngrediente.setText(QCoreApplication.translate("OrdenRequest", u"Buscar", None))
        self.botonAgregarIngrediente.setText(QCoreApplication.translate("OrdenRequest", u"Agregar", None))
        self.botonRetirarIngrediente.setText(QCoreApplication.translate("OrdenRequest", u"Retirar", None))
        self.label.setText(QCoreApplication.translate("OrdenRequest", u"Nombre del plato", None))
        self.nombrePlatoIngrediente.setText("")
        self.nombrePlatoIngrediente.setPlaceholderText(QCoreApplication.translate("OrdenRequest", u"Escribe aqui el nombre", None))
        self.label_3.setText(QCoreApplication.translate("OrdenRequest", u"Precio", None))
        self.precioPlatoIngrediente.setText("")
        self.precioPlatoIngrediente.setPlaceholderText(QCoreApplication.translate("OrdenRequest", u"Escribe aqui el precio", None))
        self.label_2.setText(QCoreApplication.translate("OrdenRequest", u"En lugar de usar espacios en los nombres, usar \"_\" ", None))
    # retranslateUi

