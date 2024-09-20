##############################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_DialogoAddInventario(object):
    def setupUi(self, DialogoAddInventario):
        if not DialogoAddInventario.objectName():
            DialogoAddInventario.setObjectName(u"DialogoAddInventario")
        DialogoAddInventario.resize(400, 300)
        DialogoAddInventario.setSizeGripEnabled(False)
        self.BotonesFormAI = QDialogButtonBox(DialogoAddInventario)
        self.BotonesFormAI.setObjectName(u"BotonesFormAI")
        self.BotonesFormAI.setGeometry(QRect(30, 240, 341, 32))
        self.BotonesFormAI.setOrientation(Qt.Horizontal)
        self.BotonesFormAI.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.layoutWidget = QWidget(DialogoAddInventario)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 29, 371, 181))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.LineEditNombreAI = QLineEdit(self.layoutWidget)
        self.LineEditNombreAI.setObjectName(u"LineEditNombreAI")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LineEditNombreAI.sizePolicy().hasHeightForWidth())
        self.LineEditNombreAI.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.LineEditNombreAI)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.LineEditCantidadAI = QLineEdit(self.layoutWidget)
        self.LineEditCantidadAI.setObjectName(u"LineEditCantidadAI")
        sizePolicy1.setHeightForWidth(self.LineEditCantidadAI.sizePolicy().hasHeightForWidth())
        self.LineEditCantidadAI.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.LineEditCantidadAI)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.lineEditUnidadDeMedidaAI = QLineEdit(self.layoutWidget)
        self.lineEditUnidadDeMedidaAI.setObjectName(u"lineEditUnidadDeMedidaAI")
        sizePolicy1.setHeightForWidth(self.lineEditUnidadDeMedidaAI.sizePolicy().hasHeightForWidth())
        self.lineEditUnidadDeMedidaAI.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEditUnidadDeMedidaAI)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.LineaAutorAI = QLineEdit(self.layoutWidget)
        self.LineaAutorAI.setObjectName(u"LineaAutorAI")
        sizePolicy1.setHeightForWidth(self.LineaAutorAI.sizePolicy().hasHeightForWidth())
        self.LineaAutorAI.setSizePolicy(sizePolicy1)
        self.LineaAutorAI.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.LineaAutorAI)

        self.label_4 = QLabel(DialogoAddInventario)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 281, 16))
        font1 = QFont()
        font1.setBold(True)
        self.label_4.setFont(font1)

        self.retranslateUi(DialogoAddInventario)
        self.BotonesFormAI.accepted.connect(DialogoAddInventario.accept)
        self.BotonesFormAI.rejected.connect(DialogoAddInventario.reject)

        QMetaObject.connectSlotsByName(DialogoAddInventario)
    # setupUi

    def retranslateUi(self, DialogoAddInventario):
        DialogoAddInventario.setWindowTitle(QCoreApplication.translate("DialogoAddInventario", u"Añadir objeto al inventario", None))
        self.label_3.setText(QCoreApplication.translate("DialogoAddInventario", u"Nombre", None))
        self.label.setText(QCoreApplication.translate("DialogoAddInventario", u"Cantidad", None))
        self.label_2.setText(QCoreApplication.translate("DialogoAddInventario", u"Und. de Medida (Kg,Lt..)", None))
        self.label_7.setText(QCoreApplication.translate("DialogoAddInventario", u"Autorizacion", None))
        self.label_4.setText(QCoreApplication.translate("DialogoAddInventario", u"En lugar de usar espacios en el nombre usar \"_\"", None))
    # retranslateUi

