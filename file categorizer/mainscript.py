from PySide6.QtWidgets import QApplication, QFrame, QGridLayout, QMainWindow, QSizePolicy, QPushButton, QWidget, QLineEdit, QDialog, QTextEdit, QFileDialog, QLabel, QSplitter
from PySide6.QtGui import QIcon, QAction, QPixmap
from PySide6.QtCore import *
import sys


app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("Categorizer")
        self.setCentralWidget(layout.mainframe)
    
class layout():
    mainframelayout = QGridLayout()
    mainframe = QFrame()

    mainframe.setLayout(mainframelayout)

class widgets():
    pass

class functions():
    pass

mainwind = MainWindow()
mainwind.show()
app.exec()