
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_orden(object):
    def setupUi(self, OrdenRequest):
        if not OrdenRequest.objectName():
            OrdenRequest.setObjectName(u"OrdenRequest")
        OrdenRequest.resize(633, 534)
        self.buttonBox = QDialogButtonBox(OrdenRequest)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(270, 490, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label_2 = QLabel(OrdenRequest)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(350, 50, 81, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.tablaOrden = QTableWidget(OrdenRequest)
        if (self.tablaOrden.columnCount() < 2):
            self.tablaOrden.setColumnCount(2)
        font1 = QFont()
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tablaOrden.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tablaOrden.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tablaOrden.setObjectName(u"tablaOrden")
        self.tablaOrden.setGeometry(QRect(10, 50, 281, 411))
        self.tablaOrden.setMinimumSize(QSize(281, 411))
        self.tablaOrden.setGridStyle(Qt.CustomDashLine)
        self.tablaOrden.horizontalHeader().setDefaultSectionSize(150)
        self.tablaOrden.horizontalHeader().setStretchLastSection(False)
        self.tablaOrden.verticalHeader().setCascadingSectionResizes(False)
        self.tablaOrden.verticalHeader().setDefaultSectionSize(32)
        self.layoutWidget = QWidget(OrdenRequest)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(350, 70, 261, 331))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.listOrden = QListWidget(self.layoutWidget)
        self.listOrden.setObjectName(u"listOrden")

        self.verticalLayout.addWidget(self.listOrden)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.lineaPrecioOrdenRe = QLineEdit(self.layoutWidget)
        self.lineaPrecioOrdenRe.setObjectName(u"lineaPrecioOrdenRe")
        self.lineaPrecioOrdenRe.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineaPrecioOrdenRe)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.layoutWidget1 = QWidget(OrdenRequest)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 321, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.buscadorOrdenRe = QLineEdit(self.layoutWidget1)
        self.buscadorOrdenRe.setObjectName(u"buscadorOrdenRe")
        self.buscadorOrdenRe.setFont(font1)

        self.horizontalLayout_2.addWidget(self.buscadorOrdenRe)

        self.botonBusquedaOrdenRe = QPushButton(self.layoutWidget1)
        self.botonBusquedaOrdenRe.setObjectName(u"botonBusquedaOrdenRe")
        self.botonBusquedaOrdenRe.setFont(font1)

        self.horizontalLayout_2.addWidget(self.botonBusquedaOrdenRe)

        self.widget = QWidget(OrdenRequest)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(130, 470, 158, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.botonAgregarPlatoOrden = QPushButton(self.widget)
        self.botonAgregarPlatoOrden.setObjectName(u"botonAgregarPlatoOrden")
        self.botonAgregarPlatoOrden.setFont(font1)

        self.horizontalLayout_3.addWidget(self.botonAgregarPlatoOrden)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.retranslateUi(OrdenRequest)
        self.buttonBox.accepted.connect(OrdenRequest.accept)
        self.buttonBox.rejected.connect(OrdenRequest.reject)

        QMetaObject.connectSlotsByName(OrdenRequest)
    # setupUi

    def retranslateUi(self, OrdenRequest):
        OrdenRequest.setWindowTitle(QCoreApplication.translate("OrdenRequest", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("OrdenRequest", u"Orden ", None))
        ___qtablewidgetitem = self.tablaOrden.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("OrdenRequest", u"Nombre", None));
        ___qtablewidgetitem1 = self.tablaOrden.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("OrdenRequest", u"Precio", None));
        self.label.setText(QCoreApplication.translate("OrdenRequest", u"Valor total a pagar ", None))
        self.buscadorOrdenRe.setText("")
        self.buscadorOrdenRe.setPlaceholderText(QCoreApplication.translate("OrdenRequest", u"Escribe aqui el nombre del plato", None))
        self.botonBusquedaOrdenRe.setText(QCoreApplication.translate("OrdenRequest", u"Buscar", None))
        self.botonAgregarPlatoOrden.setText(QCoreApplication.translate("OrdenRequest", u"Agregar", None))
        self.pushButton.setText(QCoreApplication.translate("OrdenRequest", u"Retirar", None))
    # retranslateUi

