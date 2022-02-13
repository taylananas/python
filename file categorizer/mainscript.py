from PySide6.QtWidgets import QApplication, QFrame, QGridLayout, QMainWindow, QSizePolicy, QPushButton, QWidget, QLineEdit, QDialog, QTextEdit, QFileDialog, QLabel, QSplitter
from PySide6.QtGui import QIcon, QAction, QPixmap
from PySide6.QtCore import *
import sys
import os


app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("Categorizer")
        self.setCentralWidget(layout.mainframe)

class functions():
    def filepath_select():
        global filepath
        filepath = QFileDialog.getExistingDirectory(None)
        widgets.path_label.setText(filepath)

class widgets():
    path_label = QLineEdit()
    path_label.setReadOnly(True)
    path_label.setMinimumWidth(150)
    path_label.setMaximumWidth(300)
    path_button = QPushButton("Select Folder")
    path_button.clicked.connect(functions.filepath_select)
    label_1 = QLabel("Filepath")
    
class layout():
    mainframelayout = QGridLayout()
    mainframe = QFrame()

    pathframe = QFrame()
    pathframelayout = QGridLayout()
    pathframelayout.addWidget(widgets.label_1,0,0)
    pathframelayout.addWidget(widgets.path_label,0,1)
    pathframelayout.addWidget(widgets.path_button,0,2)
    pathframe.setLayout(pathframelayout)

    mainframelayout.addWidget(pathframe)

    mainframe.setLayout(mainframelayout) 

mainwind = MainWindow()
mainwind.show()
app.exec()