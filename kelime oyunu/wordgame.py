from PySide6.QtWidgets import QApplication, QFrame, QGridLayout, QMainWindow, QTabWidget, QSizePolicy, QPushButton, QWidget, QLineEdit, QDialog, QTextEdit, QFileDialog, QLabel, QSplitter
from PySide6.QtGui import QIcon, QAction, QPixmap, QFont, QMouseEvent
from PySide6.QtCore import *
import sys

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

class widgets():
    pass

class functions():
    pass

class layout():
    pass

mainwind = MainWindow()
mainwind.show()
app.exec()
