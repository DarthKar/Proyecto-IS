

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QDoubleSpinBox, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_EditarInv(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 308)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 371, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)

        self.horizontalLayout.addWidget(self.label_9)

        self.LineEditBuscarRE = QLineEdit(self.layoutWidget)
        self.LineEditBuscarRE.setObjectName(u"LineEditBuscarRE")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LineEditBuscarRE.sizePolicy().hasHeightForWidth())
        self.LineEditBuscarRE.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.LineEditBuscarRE)

        self.buscarBotonRE = QPushButton(self.layoutWidget)
        self.buscarBotonRE.setObjectName(u"buscarBotonRE")
        sizePolicy1.setHeightForWidth(self.buscarBotonRE.sizePolicy().hasHeightForWidth())
        self.buscarBotonRE.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.buscarBotonRE)

        self.layoutWidget_2 = QWidget(Dialog)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 110, 371, 121))
        self.formLayout = QFormLayout(self.layoutWidget_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget_2)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEditUnidadDeMedidaRE = QLineEdit(self.layoutWidget_2)
        self.lineEditUnidadDeMedidaRE.setObjectName(u"lineEditUnidadDeMedidaRE")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEditUnidadDeMedidaRE.sizePolicy().hasHeightForWidth())
        self.lineEditUnidadDeMedidaRE.setSizePolicy(sizePolicy3)
        self.lineEditUnidadDeMedidaRE.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditUnidadDeMedidaRE)

        self.label_7 = QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.LineaAutorRE = QLineEdit(self.layoutWidget_2)
        self.LineaAutorRE.setObjectName(u"LineaAutorRE")
        sizePolicy3.setHeightForWidth(self.LineaAutorRE.sizePolicy().hasHeightForWidth())
        self.LineaAutorRE.setSizePolicy(sizePolicy3)
        self.LineaAutorRE.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.LineaAutorRE)

        self.doubleSpinBoxRE = QDoubleSpinBox(self.layoutWidget_2)
        self.doubleSpinBoxRE.setObjectName(u"doubleSpinBoxRE")
        self.doubleSpinBoxRE.setMaximum(100000000000000.000000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBoxRE)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Añadir Inventario", u"Añadir Inventario", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.buscarBotonRE.setText(QCoreApplication.translate("Dialog", u"Buscar", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"A\u00f1adir Cantidad", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Und. de Medida (Kg,Lt..)", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Autorizacion", None))
    # retranslateUi

