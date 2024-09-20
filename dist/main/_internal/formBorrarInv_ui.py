from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_BorrarInv(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 110, 371, 121))
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

        self.LineEditDEnombre = QLineEdit(self.layoutWidget)
        self.LineEditDEnombre.setObjectName(u"LineEditDEnombre")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LineEditDEnombre.sizePolicy().hasHeightForWidth())
        self.LineEditDEnombre.setSizePolicy(sizePolicy1)
        self.LineEditDEnombre.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.LineEditDEnombre)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.LineEditCantidadDE = QLineEdit(self.layoutWidget)
        self.LineEditCantidadDE.setObjectName(u"LineEditCantidadDE")
        sizePolicy1.setHeightForWidth(self.LineEditCantidadDE.sizePolicy().hasHeightForWidth())
        self.LineEditCantidadDE.setSizePolicy(sizePolicy1)
        self.LineEditCantidadDE.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.LineEditCantidadDE)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.lineEditUnidadDeMedidaDE = QLineEdit(self.layoutWidget)
        self.lineEditUnidadDeMedidaDE.setObjectName(u"lineEditUnidadDeMedidaDE")
        sizePolicy1.setHeightForWidth(self.lineEditUnidadDeMedidaDE.sizePolicy().hasHeightForWidth())
        self.lineEditUnidadDeMedidaDE.setSizePolicy(sizePolicy1)
        self.lineEditUnidadDeMedidaDE.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEditUnidadDeMedidaDE)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.LineaAutorDE = QLineEdit(self.layoutWidget)
        self.LineaAutorDE.setObjectName(u"LineaAutorDE")
        sizePolicy1.setHeightForWidth(self.LineaAutorDE.sizePolicy().hasHeightForWidth())
        self.LineaAutorDE.setSizePolicy(sizePolicy1)
        self.LineaAutorDE.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.LineaAutorDE)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(21, 30, 371, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget1)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setFont(font)

        self.horizontalLayout.addWidget(self.label_9)

        self.LineEditBuscarDE = QLineEdit(self.layoutWidget1)
        self.LineEditBuscarDE.setObjectName(u"LineEditBuscarDE")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.LineEditBuscarDE.sizePolicy().hasHeightForWidth())
        self.LineEditBuscarDE.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.LineEditBuscarDE)

        self.buscarBotonDE = QPushButton(self.layoutWidget1)
        self.buscarBotonDE.setObjectName(u"buscarBotonDE")
        sizePolicy3.setHeightForWidth(self.buscarBotonDE.sizePolicy().hasHeightForWidth())
        self.buscarBotonDE.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.buscarBotonDE)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Borrar Objeto", u"Borrar Objeto", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Cantidad", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Und. de Medida (Kg,Lt..)", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Autorizacion", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.buscarBotonDE.setText(QCoreApplication.translate("Dialog", u"Buscar", None))
    # retranslateUi

