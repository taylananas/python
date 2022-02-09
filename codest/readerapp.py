from PySide6.QtWidgets import QApplication, QFrame, QGridLayout, QMainWindow, QSizePolicy, QPushButton, QWidget, QLineEdit, QDialog, QTextEdit, QFileDialog, QLabel, QSplitter
from PySide6.QtGui import QIcon, QAction, QPixmap
from PySide6.QtCore import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("Reader")
        self.setGeometry(360,140,1200,800)
        self.setlayout()
    def setmenu(self):
        pass

    def setlayout(self):
        mainbuttonslayout = QGridLayout()
        mainbuttonslayout.addWidget(widgets.button1,0,0)
        mainbuttonslayout.addWidget(widgets.button2,1,0)
        mainbuttonslayout.addWidget(widgets.button3,2,0)
        mainbuttonslayout.addWidget(widgets.button4,3,0)
        mainbuttonslayout.addWidget(widgets.button5,4,0)
        mainbuttonslayout.addWidget(widgets.button6,5,0)

        mainbuttonsframe = QFrame()
        mainbuttonsframe.setFrameStyle(QFrame.Box | QFrame.Raised)
        mainbuttonsframe.setLayout(mainbuttonslayout)

        variableframe = QFrame()
        variableframe.setFrameStyle(QFrame.Box | QFrame.Raised)
        variableframelayout = QGridLayout()
        variableframe.setLayout(variableframelayout)

        historyframe = QFrame()
        historyframe.setFrameStyle(QFrame.Box | QFrame.Raised)
        historyframelayout = QGridLayout()
        historyframelayout.addWidget(widgets.historytextbox)
        historyframe.setLayout(historyframelayout)

        widgets.splitter2.addWidget(variableframe)
        widgets.splitter2.addWidget(historyframe)

        histvariframe = QFrame()
        histvariframe.setFrameStyle(QFrame.Box | QFrame.Raised)
        histvarilayout = QGridLayout()
        histvarilayout.addWidget(widgets.splitter2)
        histvariframe.setLayout(histvarilayout)

        imageframe = QFrame()
        imageframe.setFrameStyle(QFrame.Box | QFrame.Raised)
        imageframelayout = QGridLayout()
        imageframe.setMinimumWidth(400)
        imageframe.setLayout(imageframelayout)
        imageframelayout.addWidget(widgets.exampic)

        widgets.splitter1.addWidget(histvariframe)
        widgets.splitter1.addWidget(imageframe)

        frameLayout = QGridLayout()
        frameLayout.addWidget(mainbuttonsframe,0,0,2,1)
        frameLayout.addWidget(widgets.splitter1,0,2,2,1)
        mainframe = QWidget()
        mainframe.setLayout(frameLayout)

        self.setCentralWidget(mainframe)

app = QApplication(sys.argv)

class functions():
    def imageselection():
        filepath = QFileDialog.getOpenFileName(None, 'Select file', 'c:\\',"Image files (*.jpg *.png)")
        widgets.exampic.setPixmap(QPixmap(filepath[0])) 
        widgets.exampic.show()   

class widgets():    
    button1 = QPushButton("1") #button to select file
    button2 = QPushButton("2")
    button3 = QPushButton("3")
    button4 = QPushButton("4")
    button5 = QPushButton("5")
    button6 = QPushButton("6")
    button1.setFixedSize(100,100)
    button2.setFixedSize(100,100)
    button3.setFixedSize(100,100)
    button4.setFixedSize(100,100)
    button5.setFixedSize(100,100)
    button6.setFixedSize(100,100)
    button1.clicked.connect(functions.imageselection)
    historytextbox = QTextEdit()
    historytextbox.setReadOnly(True)
    testtexting = QTextEdit()
    exampic = QLabel()
    splitter1 = QSplitter(Qt.Horizontal)
    splitter2 = QSplitter(Qt.Vertical)


mainwind = MainWindow()
mainwind.show()
app.exec()