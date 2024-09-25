
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QDoubleSpinBox, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_ingredienteC(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(320, 142)
        self.botonesAc = QDialogButtonBox(Dialog)
        self.botonesAc.setObjectName(u"botonesAc")
        self.botonesAc.setGeometry(QRect(-40, 100, 341, 32))
        self.botonesAc.setOrientation(Qt.Horizontal)
        self.botonesAc.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 268, 50))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.nombreIngredienteAc = QLineEdit(self.widget)
        self.nombreIngredienteAc.setObjectName(u"nombreIngredienteAc")
        self.nombreIngredienteAc.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nombreIngredienteAc)

        self.medidaIngredienteAc = QLineEdit(self.widget)
        self.medidaIngredienteAc.setObjectName(u"medidaIngredienteAc")
        self.medidaIngredienteAc.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.medidaIngredienteAc)

        self.spinboxCantidad = QDoubleSpinBox(self.widget)
        self.spinboxCantidad.setObjectName(u"spinboxCantidad")
        self.spinboxCantidad.setMaximum(100000000000000.000000000000000)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.spinboxCantidad)


        self.retranslateUi(Dialog)
        self.botonesAc.accepted.connect(Dialog.accept)
        self.botonesAc.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Asigna la cantidad de: ", None))
    # retranslateUi

