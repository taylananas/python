from PySide6.QtWidgets import QApplication, QFrame, QGridLayout, QMainWindow, QPushButton, QWidget, QLineEdit, QDialog, QTextEdit, QFileDialog
from PySide6.QtGui import QIcon, QAction
import os
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("Reader")
        self.setGeometry(360,140,1200,800)
    
    def setmenu(self):
        pass

    def setlayout(self):
        pass

app = QApplication(sys.argv)

class functions():
    pass

class widgets():
    pass

mainwind = MainWindow()
mainwind.show()
app.exec()