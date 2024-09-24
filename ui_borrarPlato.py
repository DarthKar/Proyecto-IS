
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QWidget)

class Ui_borrarPlato(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.botonesBorrarPlato = QDialogButtonBox(Dialog)
        self.botonesBorrarPlato.setObjectName(u"botonesBorrarPlato")
        self.botonesBorrarPlato.setGeometry(QRect(40, 260, 341, 32))
        self.botonesBorrarPlato.setOrientation(Qt.Horizontal)
        self.botonesBorrarPlato.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(21, 30, 371, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)

        self.horizontalLayout.addWidget(self.label_9)

        self.LineEditBuscarDE = QLineEdit(self.layoutWidget)
        self.LineEditBuscarDE.setObjectName(u"LineEditBuscarDE")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LineEditBuscarDE.sizePolicy().hasHeightForWidth())
        self.LineEditBuscarDE.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.LineEditBuscarDE)

        self.buscarBotonDE = QPushButton(self.layoutWidget)
        self.buscarBotonDE.setObjectName(u"buscarBotonDE")
        sizePolicy1.setHeightForWidth(self.buscarBotonDE.sizePolicy().hasHeightForWidth())
        self.buscarBotonDE.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.buscarBotonDE)

        self.listWidget = QListWidget(Dialog)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(100, 70, 281, 171))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 70, 44, 20))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setFont(font)

        self.retranslateUi(Dialog)
        self.botonesBorrarPlato.accepted.connect(Dialog.accept)
        self.botonesBorrarPlato.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.buscarBotonDE.setText(QCoreApplication.translate("Dialog", u"Buscar", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Receta", None))
    # retranslateUi

