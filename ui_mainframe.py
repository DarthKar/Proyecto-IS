from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)


class Ui_mainframe(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(849, 656)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.nombre_iconos_widget = QWidget(self.centralwidget)
        self.nombre_iconos_widget.setObjectName(u"nombre_iconos_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nombre_iconos_widget.sizePolicy().hasHeightForWidth())
        self.nombre_iconos_widget.setSizePolicy(sizePolicy)
        self.nombre_iconos_widget.setStyleSheet(u"QWidget{\n"
"\n"
"background-color:rgb(0,0,0);\n"
"color:white\n"
"\n"
"}\n"
"QPushButton{\n"
"	color:white;\n"
"	text-align:left;\n"
"	height:30px;\n"
"	border:none;\n"
"	padding-left:10px;	\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	color:rgb(0,0,0);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.nombre_iconos_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.nombre_iconos_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.nombre_iconos_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 22, -1, -1)
        self.Ordenes_boton_exp = QPushButton(self.nombre_iconos_widget)
        self.Ordenes_boton_exp.setObjectName(u"Ordenes_boton_exp")
        font1 = QFont()
        font1.setPointSize(12)
        self.Ordenes_boton_exp.setFont(font1)
        self.Ordenes_boton_exp.setCursor(QCursor(Qt.PointingHandCursor))
        self.Ordenes_boton_exp.setStyleSheet(u"")
        self.Ordenes_boton_exp.setCheckable(True)
        self.Ordenes_boton_exp.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Ordenes_boton_exp)

        self.Inventario_boton_exp = QPushButton(self.nombre_iconos_widget)
        self.Inventario_boton_exp.setObjectName(u"Inventario_boton_exp")
        self.Inventario_boton_exp.setFont(font1)
        self.Inventario_boton_exp.setCursor(QCursor(Qt.PointingHandCursor))
        self.Inventario_boton_exp.setCheckable(True)
        self.Inventario_boton_exp.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Inventario_boton_exp)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_6.setContentsMargins(-1, -1, 9, -1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 289, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.BotonSalir = QPushButton(self.nombre_iconos_widget)
        self.BotonSalir.setObjectName(u"BotonSalir")
        self.BotonSalir.setCheckable(True)

        self.verticalLayout_4.addWidget(self.BotonSalir)


        self.gridLayout.addWidget(self.nombre_iconos_widget, 0, 1, 1, 1)

        self.solo_iconos_widget = QWidget(self.centralwidget)
        self.solo_iconos_widget.setObjectName(u"solo_iconos_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.solo_iconos_widget.sizePolicy().hasHeightForWidth())
        self.solo_iconos_widget.setSizePolicy(sizePolicy1)
        
        self.verticalLayout_3 = QVBoxLayout(self.solo_iconos_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(self.solo_iconos_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetFixedSize)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.Ordenes_boton_s = QPushButton(self.solo_iconos_widget)
        self.Ordenes_boton_s.setObjectName(u"Ordenes_boton_s")
        self.Ordenes_boton_s.setMinimumSize(QSize(40, 0))
        self.Ordenes_boton_s.setCursor(QCursor(Qt.PointingHandCursor))

        self.Ordenes_boton_s.setCheckable(True)
        self.Ordenes_boton_s.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Ordenes_boton_s)

        self.Inventario_boton_s = QPushButton(self.solo_iconos_widget)
        self.Inventario_boton_s.setObjectName(u"Inventario_boton_s")
        self.Inventario_boton_s.setCursor(QCursor(Qt.PointingHandCursor))
        self.Inventario_boton_s.setCheckable(True)
        self.Inventario_boton_s.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Inventario_boton_s)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 268, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_7 = QPushButton(self.solo_iconos_widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_7)


        self.gridLayout.addWidget(self.solo_iconos_widget, 0, 0, 1, 1)

        self.menu_principal = QWidget(self.centralwidget)
        self.menu_principal.setObjectName(u"menu_principal")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.menu_principal.sizePolicy().hasHeightForWidth())
        self.menu_principal.setSizePolicy(sizePolicy2)
        self.menu_principal.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_5 = QVBoxLayout(self.menu_principal)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.menu_principal)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Ordenes = QWidget()
        self.Ordenes.setObjectName(u"Ordenes")
        self.label_5 = QLabel(self.Ordenes)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(120, 140, 331, 141))
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.stackedWidget.addWidget(self.Ordenes)
        self.Inventario = QWidget()
        self.Inventario.setObjectName(u"Inventario")
        self.label_4 = QLabel(self.Inventario)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 170, 301, 81))
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.stackedWidget.addWidget(self.Inventario)

        self.home = QWidget()
        self.home.setObjectName(u"Home")
        self.label_home = QLabel(self.home)
        self.label_home.setObjectName(u"label_home")
        self.label_home.setGeometry(QRect(140, 170, 301, 81))
        self.label_home.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_home.setText(QCoreApplication.translate("MainWindow", u"Aqui va todo lo del home", None))
        self.stackedWidget.addWidget(self.home)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.menu_principal, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menu_principal.raise_()
        self.solo_iconos_widget.raise_()
        self.nombre_iconos_widget.raise_()

        self.retranslateUi(MainWindow)
        self.Ordenes_boton_s.toggled.connect(self.Ordenes_boton_exp.setChecked)
        self.Inventario_boton_s.toggled.connect(self.Inventario_boton_exp.setChecked)
        self.Ordenes_boton_exp.toggled.connect(self.Ordenes_boton_s.setChecked)
        self.Inventario_boton_exp.toggled.connect(self.Inventario_boton_s.setChecked)
        self.pushButton_7.toggled.connect(MainWindow.close)
        self.BotonSalir.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TIF - CHIDO", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CHIDO", None))
        self.Ordenes_boton_exp.setText(QCoreApplication.translate("MainWindow", u"Ordenes", None))
        self.Inventario_boton_exp.setText(QCoreApplication.translate("MainWindow", u"Inventario", None))
        self.BotonSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.label.setText("")
        self.Ordenes_boton_s.setText("")
        self.Inventario_boton_s.setText("")
        self.pushButton_7.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Aqui va la logica de las ordenes", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Aqui va la logica del inventario ", None))


