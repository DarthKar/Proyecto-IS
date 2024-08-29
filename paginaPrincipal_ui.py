
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
import recursos_rc
import recursos_rc

class Ui_MainWindow(object):
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nombre_iconos_widget.sizePolicy().hasHeightForWidth())
        self.nombre_iconos_widget.setSizePolicy(sizePolicy)
        self.nombre_iconos_widget.setStyleSheet(u"QWidget{\n"
"\n"
"background-color:rgb(94, 172, 36);\n"
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
"	color:rgb(94, 172, 36);\n"
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
        self.label_2.setPixmap(QPixmap(u":/recursos_rc/user.png"))
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
        self.Dashboard_boton_exp = QPushButton(self.nombre_iconos_widget)
        self.Dashboard_boton_exp.setObjectName(u"Dashboard_boton_exp")
        font1 = QFont()
        font1.setPointSize(12)
        self.Dashboard_boton_exp.setFont(font1)
        self.Dashboard_boton_exp.setCursor(QCursor(Qt.PointingHandCursor))
        self.Dashboard_boton_exp.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/recursos_rc/dashboard2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/recursos_rc/dashboard.png", QSize(), QIcon.Normal, QIcon.On)
        self.Dashboard_boton_exp.setIcon(icon)
        self.Dashboard_boton_exp.setCheckable(True)
        self.Dashboard_boton_exp.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Dashboard_boton_exp)

        self.Inventario_boton_exp = QPushButton(self.nombre_iconos_widget)
        self.Inventario_boton_exp.setObjectName(u"Inventario_boton_exp")
        self.Inventario_boton_exp.setFont(font1)
        self.Inventario_boton_exp.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/recursos_rc/databas2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/recursos_rc/database.png", QSize(), QIcon.Normal, QIcon.On)
        self.Inventario_boton_exp.setIcon(icon1)
        self.Inventario_boton_exp.setCheckable(True)
        self.Inventario_boton_exp.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Inventario_boton_exp)

        self.Exportar_boton_exp = QPushButton(self.nombre_iconos_widget)
        self.Exportar_boton_exp.setObjectName(u"Exportar_boton_exp")
        self.Exportar_boton_exp.setFont(font1)
        self.Exportar_boton_exp.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/recursos_rc/share2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/recursos_rc/share.png", QSize(), QIcon.Normal, QIcon.On)
        self.Exportar_boton_exp.setIcon(icon2)
        self.Exportar_boton_exp.setCheckable(True)
        self.Exportar_boton_exp.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Exportar_boton_exp)

        self.Ajustes_boton_exp = QPushButton(self.nombre_iconos_widget)
        self.Ajustes_boton_exp.setObjectName(u"Ajustes_boton_exp")
        self.Ajustes_boton_exp.setFont(font1)
        self.Ajustes_boton_exp.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/recursos_rc/setting2.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/recursos_rc/setting.png", QSize(), QIcon.Normal, QIcon.On)
        self.Ajustes_boton_exp.setIcon(icon3)
        self.Ajustes_boton_exp.setCheckable(True)
        self.Ajustes_boton_exp.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Ajustes_boton_exp)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_6.setContentsMargins(-1, -1, 9, -1)
        self.label_9 = QLabel(self.nombre_iconos_widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(75, 16777215))
        self.label_9.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.pushButton = QPushButton(self.nombre_iconos_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(20, 20))
        self.pushButton.setMaximumSize(QSize(20, 20))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
" border-radius: 10px;\n"
" border: 1px solid; ")

        self.horizontalLayout_6.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 289, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.pushButton_13 = QPushButton(self.nombre_iconos_widget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        icon4 = QIcon()
        icon4.addFile(u":/recursos_rc/log-out2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon4)
        self.pushButton_13.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_13)


        self.gridLayout.addWidget(self.nombre_iconos_widget, 0, 1, 1, 1)

        self.solo_iconos_widget = QWidget(self.centralwidget)
        self.solo_iconos_widget.setObjectName(u"solo_iconos_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.solo_iconos_widget.sizePolicy().hasHeightForWidth())
        self.solo_iconos_widget.setSizePolicy(sizePolicy1)
        self.solo_iconos_widget.setStyleSheet(u"QWidget{\n"
"background-color:rgb(94, 172, 36);\n"
"}\n"
"QPushButton{\n"
"	color:white;\n"
"	text-align:centert;\n"
"	height:30px;\n"
"	border:none;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	color:rgb(94, 172, 36);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.solo_iconos_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(self.solo_iconos_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/recursos_rc/user.png"))
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
        self.DashBoard_boton_s = QPushButton(self.solo_iconos_widget)
        self.DashBoard_boton_s.setObjectName(u"DashBoard_boton_s")
        self.DashBoard_boton_s.setMinimumSize(QSize(40, 0))
        self.DashBoard_boton_s.setCursor(QCursor(Qt.PointingHandCursor))
        self.DashBoard_boton_s.setIcon(icon)
        self.DashBoard_boton_s.setCheckable(True)
        self.DashBoard_boton_s.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.DashBoard_boton_s)

        self.Inventario_boton_s = QPushButton(self.solo_iconos_widget)
        self.Inventario_boton_s.setObjectName(u"Inventario_boton_s")
        self.Inventario_boton_s.setCursor(QCursor(Qt.PointingHandCursor))
        self.Inventario_boton_s.setIcon(icon1)
        self.Inventario_boton_s.setCheckable(True)
        self.Inventario_boton_s.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Inventario_boton_s)

        self.Exportar_boton_s = QPushButton(self.solo_iconos_widget)
        self.Exportar_boton_s.setObjectName(u"Exportar_boton_s")
        self.Exportar_boton_s.setCursor(QCursor(Qt.PointingHandCursor))
        self.Exportar_boton_s.setIcon(icon2)
        self.Exportar_boton_s.setCheckable(True)
        self.Exportar_boton_s.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Exportar_boton_s)

        self.Ajustes_boton_s = QPushButton(self.solo_iconos_widget)
        self.Ajustes_boton_s.setObjectName(u"Ajustes_boton_s")
        self.Ajustes_boton_s.setCursor(QCursor(Qt.PointingHandCursor))
        self.Ajustes_boton_s.setIcon(icon3)
        self.Ajustes_boton_s.setCheckable(True)
        self.Ajustes_boton_s.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Ajustes_boton_s)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 268, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_7 = QPushButton(self.solo_iconos_widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setIcon(icon4)
        self.pushButton_7.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_7)


        self.gridLayout.addWidget(self.solo_iconos_widget, 0, 0, 1, 1)

        self.menu_principal = QWidget(self.centralwidget)
        self.menu_principal.setObjectName(u"menu_principal")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.menu_principal.sizePolicy().hasHeightForWidth())
        self.menu_principal.setSizePolicy(sizePolicy2)
        self.menu_principal.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_5 = QVBoxLayout(self.menu_principal)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.encabezado_widget = QWidget(self.menu_principal)
        self.encabezado_widget.setObjectName(u"encabezado_widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.encabezado_widget.sizePolicy().hasHeightForWidth())
        self.encabezado_widget.setSizePolicy(sizePolicy3)
        self.horizontalLayout_4 = QHBoxLayout(self.encabezado_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.BotonMenuDesp = QPushButton(self.encabezado_widget)
        self.BotonMenuDesp.setObjectName(u"BotonMenuDesp")
        self.BotonMenuDesp.setCursor(QCursor(Qt.PointingHandCursor))
        self.BotonMenuDesp.setStyleSheet(u"QPushButton#BotonMenuDesp{\n"
"border-radius:10px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/recursos_rc/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BotonMenuDesp.setIcon(icon5)
        self.BotonMenuDesp.setIconSize(QSize(20, 20))
        self.BotonMenuDesp.setCheckable(True)
        self.BotonMenuDesp.setAutoExclusive(False)

        self.horizontalLayout_4.addWidget(self.BotonMenuDesp)

        self.horizontalSpacer_3 = QSpacerItem(152, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.encabezado_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_15 = QPushButton(self.encabezado_widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/recursos_rc/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon6)
        self.pushButton_15.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton_15)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer_4 = QSpacerItem(152, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.actualizarBoton = QPushButton(self.encabezado_widget)
        self.actualizarBoton.setObjectName(u"actualizarBoton")
        self.actualizarBoton.setCursor(QCursor(Qt.PointingHandCursor))
        self.actualizarBoton.setStyleSheet(u".QPushButton#actualizarBoton{\n"
"background-color:rgb(94, 172, 36);\n"
"color:White;\n"
"padding: 5px 10px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"font-size: 12px;\n"
"border-radius: 5px; \n"
"border: 2px solid;\n"
"}\n"
"QPushButton#actualizarBoton:hover {\n"
"  background-color: rgba(0, 0, 0, 0.1);\n"
"  color:Black;\n"
"}")

        self.horizontalLayout_4.addWidget(self.actualizarBoton)


        self.verticalLayout_5.addWidget(self.encabezado_widget)

        self.stackedWidget = QStackedWidget(self.menu_principal)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.DashBoar_page = QWidget()
        self.DashBoar_page.setObjectName(u"DashBoar_page")
        self.tablaOrdenes = QTableWidget(self.DashBoar_page)
        if (self.tablaOrdenes.columnCount() < 4):
            self.tablaOrdenes.setColumnCount(4)
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.tablaOrdenes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(True)
        font3.setStyleStrategy(QFont.PreferDefault)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        self.tablaOrdenes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.tablaOrdenes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.tablaOrdenes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tablaOrdenes.setObjectName(u"tablaOrdenes")
        self.tablaOrdenes.setGeometry(QRect(270, 40, 381, 491))
        sizePolicy3.setHeightForWidth(self.tablaOrdenes.sizePolicy().hasHeightForWidth())
        self.tablaOrdenes.setSizePolicy(sizePolicy3)
        self.tablaOrdenes.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.tablaOrdenes.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"QTableWidget::item:selected { background-color: blue; }\n"
" ")
        self.tablaOrdenes.setFrameShape(QFrame.Box)
        self.tablaOrdenes.setFrameShadow(QFrame.Plain)
        self.tablaOrdenes.setAlternatingRowColors(True)
        self.tablaOrdenes.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tablaOrdenes.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablaOrdenes.setGridStyle(Qt.SolidLine)
        self.tablaOrdenes.setRowCount(0)
        self.label_6 = QLabel(self.DashBoar_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(270, 20, 191, 16))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.layoutWidget = QWidget(self.DashBoar_page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 261, 200))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.genCompra = QPushButton(self.layoutWidget)
        self.genCompra.setObjectName(u"genCompra")
        font5 = QFont()
        font5.setBold(True)
        font5.setUnderline(False)
        font5.setStrikeOut(False)
        self.genCompra.setFont(font5)
        self.genCompra.setStyleSheet(u".QPushButton#genCompra{\n"
"background-color:rgb(94, 172, 36);\n"
"color:White;\n"
"padding: 10px 20px; \n"
"text-align: center;\n"
"text-decoration: none;\n"
"font-size: 16px;\n"
"border-radius: 5px; \n"
"border: 2px solid; \n"
"}\n"
"QPushButton#genCompra:hover {\n"
"  background-color: rgba(0, 0, 0, 0.1);\n"
"  color:Black;\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.genCompra)

        self.genVal = QPushButton(self.layoutWidget)
        self.genVal.setObjectName(u"genVal")
        self.genVal.setFont(font5)
        self.genVal.setStyleSheet(u".QPushButton#genVal{\n"
"background-color:rgb(94, 172, 36);\n"
"color:White;\n"
"padding: 10px 20px; \n"
"text-align: center;\n"
"text-decoration: none;\n"
"font-size: 16px;\n"
"border-radius: 5px; \n"
"border: 2px solid; \n"
"}\n"
"QPushButton#genVal:hover {\n"
"  background-color: rgba(0, 0, 0, 0.1);\n"
"  color:Black;\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.genVal)

        self.retirarOrden = QPushButton(self.layoutWidget)
        self.retirarOrden.setObjectName(u"retirarOrden")
        self.retirarOrden.setFont(font5)
        self.retirarOrden.setStyleSheet(u".QPushButton#retirarOrden{\n"
"background-color:rgb(94, 172, 36);\n"
"color:White;\n"
"padding: 10px 20px; \n"
"text-align: center;\n"
"text-decoration: none;\n"
"font-size: 16px;\n"
"border-radius: 5px; \n"
"border: 2px solid; \n"
"}\n"
"QPushButton#retirarOrden:hover {\n"
"  background-color: rgba(0, 0, 0, 0.1);\n"
"  color:Black;\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.retirarOrden)

        self.ordenInfoTabla = QListWidget(self.DashBoar_page)
        self.ordenInfoTabla.setObjectName(u"ordenInfoTabla")
        self.ordenInfoTabla.setGeometry(QRect(0, 250, 261, 291))
        self.ordenInfoTabla.setStyleSheet(u"\n"
"#ordenInfoTabla{\n"
"		border: 2px solid rgb(94, 172, 36); \n"
"        border-radius: 10px; /* Bordes redondeados */\n"
"        padding: 10px; /* Espaciado interno */\n"
"        background-color: #f9f9f9; /* Fondo de la lista */\n"
"		color: rgb(0, 0, 0);\n"
"    }\n"
"    #ordenInfoTabla::item {\n"
"        padding: 3px 5px; /* Espaciado interno de los elementos */\n"
"        border-bottom: 1px solid #ddd; /* L\u00ednea divisoria entre elementos */\n"
"    }\n"
"    #ordenInfoTabla::item:last-child {\n"
"        border-bottom: none; /* Elimina la l\u00ednea del \u00faltimo elemento */\n"
"    }\n"
"     #ordenInfoTabla::item:hover {\n"
"        background-color: #e6f7ff; /* Fondo azul claro al pasar el mouse */\n"
"    }")
        self.ordenInfoTabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ordenInfoTabla.setDragEnabled(False)
        self.ordenInfoTabla.setAlternatingRowColors(True)
        self.ordenInfoTabla.setSelectionMode(QAbstractItemView.NoSelection)
        self.label_8 = QLabel(self.DashBoar_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(2, 231, 136, 16))
        font6 = QFont()
        font6.setBold(True)
        self.label_8.setFont(font6)
        self.label_8.setStyleSheet(u"color:Black;")
        self.lineEditNOrden = QLineEdit(self.DashBoar_page)
        self.lineEditNOrden.setObjectName(u"lineEditNOrden")
        self.lineEditNOrden.setGeometry(QRect(140, 230, 71, 21))
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(10)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEditNOrden.sizePolicy().hasHeightForWidth())
        self.lineEditNOrden.setSizePolicy(sizePolicy4)
        self.lineEditNOrden.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.lineEditNOrden.setReadOnly(True)
        self.stackedWidget.addWidget(self.DashBoar_page)
        self.Inventario_page = QWidget()
        self.Inventario_page.setObjectName(u"Inventario_page")
        self.tableWidget = QTableWidget(self.Inventario_page)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 20, 321, 501))
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        self.tableWidget.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.tableWidget.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.tableWidget.setFrameShape(QFrame.Box)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setRowCount(0)
        self.layoutWidget1 = QWidget(self.Inventario_page)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(330, 170, 291, 323))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_6.setContentsMargins(10, 0, 0, 0)
        self.editarInventarioBoton = QPushButton(self.layoutWidget1)
        self.editarInventarioBoton.setObjectName(u"editarInventarioBoton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.editarInventarioBoton.sizePolicy().hasHeightForWidth())
        self.editarInventarioBoton.setSizePolicy(sizePolicy5)
        font7 = QFont()
        font7.setBold(True)
        font7.setItalic(False)
        font7.setUnderline(False)
        font7.setStrikeOut(False)
        self.editarInventarioBoton.setFont(font7)
        self.editarInventarioBoton.setStyleSheet(u".QPushButton#editarInventarioBoton{\n"
"background-color:rgb(94, 172, 36);\n"
"color:White;\n"
"padding: 10px 20px; \n"
"text-align: center;\n"
"text-decoration: none;\n"
"font-size: 16px;\n"
"border-radius: 5px; \n"
"border: 2px solid; \n"
"}\n"
"QPushButton#editarInventarioBoton:hover {\n"
"  background-color: rgba(0, 0, 0, 0.1);\n"
"  color:Black;\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.editarInventarioBoton)

        self.addInventarioBoton = QPushButton(self.layoutWidget1)
        self.addInventarioBoton.setObjectName(u"addInventarioBoton")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(12)
        sizePolicy6.setHeightForWidth(self.addInventarioBoton.sizePolicy().hasHeightForWidth())
        self.addInventarioBoton.setSizePolicy(sizePolicy6)
        self.addInventarioBoton.setFont(font7)
        self.addInventarioBoton.setStyleSheet(u".QPushButton#addInventarioBoton{\n"
"background-color:rgb(94, 172, 36);\n"
"color:White;\n"
"padding: 10px 20px; \n"
"text-align: center;\n"
"text-decoration: none;\n"
"font-size: 16px;\n"
"border-radius: 5px; \n"
"border: 2px solid; \n"
"}\n"
"QPushButton#addInventarioBoton:hover {\n"
"  background-color: rgba(0, 0, 0, 0.1);\n"
"  color:Black;\n"
"}")

        self.verticalLayout_6.addWidget(self.addInventarioBoton)

        self.borrarInventarioBoton = QPushButton(self.layoutWidget1)
        self.borrarInventarioBoton.setObjectName(u"borrarInventarioBoton")
        sizePolicy5.setHeightForWidth(self.borrarInventarioBoton.sizePolicy().hasHeightForWidth())
        self.borrarInventarioBoton.setSizePolicy(sizePolicy5)
        self.borrarInventarioBoton.setFont(font7)
        self.borrarInventarioBoton.setStyleSheet(u".QPushButton#borrarInventarioBoton{\n"
"background-color:rgb(94, 172, 36);\n"
"color:White;\n"
"padding: 10px 20px; \n"
"text-align: center;\n"
"text-decoration: none;\n"
"font-size: 16px;\n"
"border-radius: 5px; \n"
"border: 2px solid; \n"
"}\n"
"QPushButton#borrarInventarioBoton:hover {\n"
"  background-color: rgba(0, 0, 0, 0.1);\n"
"  color:Black;\n"
"}")

        self.verticalLayout_6.addWidget(self.borrarInventarioBoton)

        self.layoutWidget2 = QWidget(self.Inventario_page)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(330, 520, 217, 24))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        font8 = QFont()
        font8.setPointSize(10)
        self.label_5.setFont(font8)
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit_2 = QLineEdit(self.layoutWidget2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color:White;")
        self.lineEdit_2.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineEdit_2)

        self.labelInvenDis = QLabel(self.Inventario_page)
        self.labelInvenDis.setObjectName(u"labelInvenDis")
        self.labelInvenDis.setGeometry(QRect(0, 0, 191, 16))
        self.labelInvenDis.setFont(font4)
        self.labelInvenDis.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.botonTogglePlatos = QPushButton(self.Inventario_page)
        self.botonTogglePlatos.setObjectName(u"botonTogglePlatos")
        self.botonTogglePlatos.setGeometry(QRect(330, 20, 141, 30))
        self.botonTogglePlatos.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonTogglePlatos.setStyleSheet(u".QPushButton#botonTogglePlatos{\n"
"background-color:rgb(94, 172, 36);\n"
"color:White;\n"
"padding: 5px 10px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"font-size: 12px;\n"
"border-radius: 5px; \n"
"border: 2px solid;\n"
"}\n"
"QPushButton#botonTogglePlatos:hover {\n"
"  background-color: rgba(0, 0, 0, 0.1);\n"
"  color:Black;\n"
"}")
        self.listaReceta = QListWidget(self.Inventario_page)
        self.listaReceta.setObjectName(u"listaReceta")
        self.listaReceta.setGeometry(QRect(350, 110, 261, 351))
        self.listaReceta.setStyleSheet(u"\n"
"#listaReceta{\n"
"		border: 2px solid rgb(94, 172, 36); \n"
"        border-radius: 10px; /* Bordes redondeados */\n"
"        padding: 10px; /* Espaciado interno */\n"
"        background-color: #f9f9f9; /* Fondo de la lista */\n"
"		color: rgb(0, 0, 0);\n"
"    }\n"
"    #listaReceta::item {\n"
"        padding: 3px 5px; /* Espaciado interno de los elementos */\n"
"        border-bottom: 1px solid #ddd; /* L\u00ednea divisoria entre elementos */\n"
"    }\n"
"    #listaReceta::item:last-child {\n"
"        border-bottom: none; /* Elimina la l\u00ednea del \u00faltimo elemento */\n"
"    }\n"
"     #listaReceta::item:hover {\n"
"        background-color: #e6f7ff; /* Fondo azul claro al pasar el mouse */\n"
"    }")
        self.listaReceta.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listaReceta.setDragEnabled(False)
        self.listaReceta.setAlternatingRowColors(True)
        self.listaReceta.setSelectionMode(QAbstractItemView.NoSelection)
        self.tablaPlatosInv = QTableWidget(self.Inventario_page)
        if (self.tablaPlatosInv.columnCount() < 2):
            self.tablaPlatosInv.setColumnCount(2)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font2);
        self.tablaPlatosInv.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font2);
        self.tablaPlatosInv.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        self.tablaPlatosInv.setObjectName(u"tablaPlatosInv")
        self.tablaPlatosInv.setGeometry(QRect(0, 20, 321, 501))
        sizePolicy3.setHeightForWidth(self.tablaPlatosInv.sizePolicy().hasHeightForWidth())
        self.tablaPlatosInv.setSizePolicy(sizePolicy3)
        self.tablaPlatosInv.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.tablaPlatosInv.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.tablaPlatosInv.setFrameShape(QFrame.Box)
        self.tablaPlatosInv.setFrameShadow(QFrame.Plain)
        self.tablaPlatosInv.setAlternatingRowColors(True)
        self.tablaPlatosInv.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tablaPlatosInv.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablaPlatosInv.setGridStyle(Qt.SolidLine)
        self.tablaPlatosInv.setRowCount(0)
        self.tablaPlatosInv.horizontalHeader().setCascadingSectionResizes(True)
        self.tablaPlatosInv.horizontalHeader().setDefaultSectionSize(150)
        self.labelInvenDis_2 = QLabel(self.Inventario_page)
        self.labelInvenDis_2.setObjectName(u"labelInvenDis_2")
        self.labelInvenDis_2.setGeometry(QRect(350, 90, 191, 16))
        font9 = QFont()
        font9.setPointSize(10)
        font9.setBold(True)
        self.labelInvenDis_2.setFont(font9)
        self.labelInvenDis_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.stackedWidget.addWidget(self.Inventario_page)
        self.tableWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.labelInvenDis.raise_()
        self.botonTogglePlatos.raise_()
        self.tablaPlatosInv.raise_()
        self.listaReceta.raise_()
        self.labelInvenDis_2.raise_()
        self.Exportar_page = QWidget()
        self.Exportar_page.setObjectName(u"Exportar_page")
        self.botonGenInv = QPushButton(self.Exportar_page)
        self.botonGenInv.setObjectName(u"botonGenInv")
        self.botonGenInv.setGeometry(QRect(40, 40, 251, 131))
        self.botonGenInv.setFont(font5)
        self.botonGenInv.setStyleSheet(u"QPushButton#botonGenInv {\n"
"\n"
"  background-color: transparent;\n"
"  color: inherit; \n"
"  padding: 10px 20px; \n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 16px;\n"
"  border-radius: 5px; \n"
"  border: 2px solid; \n"
"}\n"
"QPushButton#botonGenInv:hover {\n"
"  background-color: rgba(0, 0, 0, 0.1);\n"
"}")
        self.botonGenVentas = QPushButton(self.Exportar_page)
        self.botonGenVentas.setObjectName(u"botonGenVentas")
        self.botonGenVentas.setGeometry(QRect(330, 40, 251, 131))
        self.botonGenVentas.setFont(font5)
        self.botonGenVentas.setStyleSheet(u"QPushButton#botonGenVentas {\n"
"\n"
"  background-color: transparent;\n"
"  color: inherit; \n"
"  padding: 10px 20px; \n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 16px;\n"
"  border-radius: 5px; \n"
"  border: 2px solid; \n"
"}\n"
"QPushButton#botonGenVentas:hover {\n"
"  background-color: rgba(0, 0, 0, 0.1);\n"
"}")
        self.stackedWidget.addWidget(self.Exportar_page)
        self.Ajustes_page = QWidget()
        self.Ajustes_page.setObjectName(u"Ajustes_page")
        self.botonAgregarPlatos = QPushButton(self.Ajustes_page)
        self.botonAgregarPlatos.setObjectName(u"botonAgregarPlatos")
        self.botonAgregarPlatos.setGeometry(QRect(330, 40, 251, 131))
        self.botonAgregarPlatos.setFont(font5)
        self.botonAgregarPlatos.setStyleSheet(u"QPushButton#botonAgregarPlatos {\n"
"\n"
"  background-color: transparent;\n"
"  color: inherit; \n"
"  padding: 10px 20px; \n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 16px;\n"
"  border-radius: 5px; \n"
"  border: 2px solid; \n"
"}\n"
"QPushButton#botonAgregarPlatos:hover {\n"
"  background-color: rgba(0, 0, 0, 0.1);\n"
"}")
        self.botonStatusCaja = QPushButton(self.Ajustes_page)
        self.botonStatusCaja.setObjectName(u"botonStatusCaja")
        self.botonStatusCaja.setGeometry(QRect(40, 40, 251, 131))
        self.botonStatusCaja.setFont(font5)
        self.botonStatusCaja.setStyleSheet(u"QPushButton#botonStatusCaja{\n"
"\n"
"  background-color: transparent;\n"
"  color: inherit; \n"
"  padding: 10px 20px; \n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 16px;\n"
"  border-radius: 5px; \n"
"  border: 2px solid; \n"
"}\n"
"QPushButton#botonStatusCaja:hover {\n"
"  background-color: rgba(0, 0, 0, 0.1);\n"
"}")
        self.stackedWidget.addWidget(self.Ajustes_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.menu_principal, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.BotonMenuDesp.toggled.connect(self.solo_iconos_widget.setHidden)
        self.BotonMenuDesp.toggled.connect(self.nombre_iconos_widget.setVisible)
        self.DashBoard_boton_s.toggled.connect(self.Dashboard_boton_exp.setChecked)
        self.Inventario_boton_s.toggled.connect(self.Inventario_boton_exp.setChecked)
        self.Exportar_boton_s.toggled.connect(self.Exportar_boton_exp.setChecked)
        self.Ajustes_boton_s.toggled.connect(self.Ajustes_boton_exp.setChecked)
        self.Dashboard_boton_exp.toggled.connect(self.DashBoard_boton_s.setChecked)
        self.Inventario_boton_exp.toggled.connect(self.Inventario_boton_s.setChecked)
        self.Exportar_boton_exp.toggled.connect(self.Exportar_boton_s.setChecked)
        self.Ajustes_boton_exp.toggled.connect(self.Ajustes_boton_s.setChecked)
        self.pushButton_7.toggled.connect(MainWindow.close)
        self.pushButton_13.toggled.connect(MainWindow.close)
        self.Dashboard_boton_exp.toggled.connect(self.lineEdit.hide)
        self.Inventario_boton_exp.toggled.connect(self.lineEdit.show)
        self.Inventario_boton_exp.toggled.connect(self.pushButton_15.show)
        self.Dashboard_boton_exp.toggled.connect(self.pushButton_15.hide)
        self.Exportar_boton_exp.toggled.connect(self.lineEdit.hide)
        self.Exportar_boton_exp.toggled.connect(self.pushButton_15.hide)
        self.Ajustes_boton_exp.toggled.connect(self.lineEdit.hide)
        self.Ajustes_boton_exp.toggled.connect(self.pushButton_15.hide)
        self.Dashboard_boton_exp.toggled.connect(self.actualizarBoton.hide)
        self.Inventario_boton_exp.toggled.connect(self.actualizarBoton.show)
        self.Exportar_boton_exp.toggled.connect(self.actualizarBoton.hide)
        self.Ajustes_boton_exp.toggled.connect(self.actualizarBoton.hide)
        self.DashBoard_boton_s.toggled.connect(self.actualizarBoton.hide)
        self.Inventario_boton_s.toggled.connect(self.actualizarBoton.show)
        self.Exportar_boton_s.toggled.connect(self.actualizarBoton.hide)
        self.Ajustes_boton_s.toggled.connect(self.actualizarBoton.hide)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CHIDO", None))
        self.Dashboard_boton_exp.setText(QCoreApplication.translate("MainWindow", u"DashBoard", None))
        self.Inventario_boton_exp.setText(QCoreApplication.translate("MainWindow", u"Inventario", None))
        self.Exportar_boton_exp.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.Ajustes_boton_exp.setText(QCoreApplication.translate("MainWindow", u"Ajustes", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Estado Caja: ", None))
        self.pushButton.setText("")
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.label.setText("")
        self.DashBoard_boton_s.setText("")
        self.Inventario_boton_s.setText("")
        self.Exportar_boton_s.setText("")
        self.Ajustes_boton_s.setText("")
        self.pushButton_7.setText("")
        self.BotonMenuDesp.setText("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_15.setText("")
        self.actualizarBoton.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        ___qtablewidgetitem = self.tablaOrdenes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 orden", None));
        ___qtablewidgetitem1 = self.tablaOrdenes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hora creacion", None));
        ___qtablewidgetitem2 = self.tablaOrdenes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Hora validacion", None));
        ___qtablewidgetitem3 = self.tablaOrdenes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Valor ", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Ordenes ", None))
        self.genCompra.setText(QCoreApplication.translate("MainWindow", u"Crear orden", None))
        self.genVal.setText(QCoreApplication.translate("MainWindow", u"Validar orden", None))
        self.retirarOrden.setText(QCoreApplication.translate("MainWindow", u"Eliminar orden", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Informacion de la orden", None))
        self.lineEditNOrden.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00b0 Orden", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Nombre ", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Und", None));
        self.editarInventarioBoton.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Inventario", None))
        self.addInventarioBoton.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Objeto", None))
        self.borrarInventarioBoton.setText(QCoreApplication.translate("MainWindow", u"Borrar Objeto", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ultima Edicion", None))
        self.lineEdit_2.setText("")
        self.labelInvenDis.setText(QCoreApplication.translate("MainWindow", u"Inventario Disponible", None))
        self.botonTogglePlatos.setText(QCoreApplication.translate("MainWindow", u"Ver Platos disponibles", None))
        ___qtablewidgetitem7 = self.tablaPlatosInv.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Nombre ", None));
        ___qtablewidgetitem8 = self.tablaPlatosInv.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Precio", None));
        self.labelInvenDis_2.setText(QCoreApplication.translate("MainWindow", u"Receta", None))
        self.botonGenInv.setText(QCoreApplication.translate("MainWindow", u"Exportar Inventario", None))
        self.botonGenVentas.setText(QCoreApplication.translate("MainWindow", u"Exportar Ventas", None))
        self.botonAgregarPlatos.setText(QCoreApplication.translate("MainWindow", u"Agregar Platos", None))
        self.botonStatusCaja.setText(QCoreApplication.translate("MainWindow", u"Abrir Caja", None))
    # retranslateUi

