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
    def setupUi(self,mainframe):
        if not mainframe.objectName():
            mainframe.setObjectName(u"mainframe")#Logica para que se genere el objeto con nombre
        mainframe.setWindowTitle("TIF - Chido") 
        mainframe.resize(800,600) #resize hace que se pueda rescalar todos los widgets que estan anclados a un tamaño que depende de su contenedor
        mainframe.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        mainframe.show()