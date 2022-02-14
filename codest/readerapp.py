from PySide6.QtWidgets import QApplication, QFrame, QGridLayout, QMainWindow, QSizePolicy, QPushButton, QWidget, QLineEdit, QDialog, QTextEdit, QFileDialog, QLabel, QSplitter
from PySide6.QtGui import QIcon, QAction, QPixmap, QFont
from PySide6.QtCore import *
import sys
from datetime import datetime

from matplotlib.pyplot import hist
app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("Reader")
        self.setGeometry(360,140,1200,800)
        self.setCentralWidget(layout.mainframe)

class functions():
    def imageselection():
        filepath = QFileDialog.getOpenFileName(None, 'Select file', 'c:\\',"Image files (*.jpg *.png *.jfif)")
        pixmap = QPixmap(filepath[0])
        widgets.exampic.setPixmap(pixmap) 
        widgets.exampic.show()   
    
    def clearvariablelayout():
        for i in reversed(range(layout.variableframelayout.count())):
            removedwidget = layout.variableframelayout.itemAt(i).widget()
            removedwidget.setParent(None)
            layout.variableframelayout.removeWidget(removedwidget)
        
        now = datetime.now().strftime("%H:%M:%S") 
        widgets.historytextbox.append(f"{now}   :   Clearing variables...")

    def test1():
        functions.clearvariablelayout()
        layout.variableframelayout.addWidget(widgets.testbut1)
        layout.variableframelayout.addWidget(widgets.testbut3)

    def test2():
        functions.clearvariablelayout()
        layout.variableframelayout.addWidget(widgets.testbut2)

class widgets():    
    button1 = QPushButton("1") #button to select file
    button2 = QPushButton("2")
    button3 = QPushButton("3")
    button4 = QPushButton("4")
    button5 = QPushButton("5")
    button6 = QPushButton("6")

    testbut1 = QPushButton("test 1")
    testbut2 = QPushButton("test 2")
    testbut3 = QPushButton("test 3")

    button1.setFixedSize(100,100)
    button2.setFixedSize(100,100)
    button3.setFixedSize(100,100)
    button4.setFixedSize(100,100)
    button5.setFixedSize(100,100)
    button6.setFixedSize(100,100)
    button1.clicked.connect(functions.imageselection)
    button2.clicked.connect(functions.test1)
    button3.clicked.connect(functions.test2)

    historytextbox = QTextEdit()
    historytextbox.setReadOnly(True)

    textfont = QFont()
    textfont.setPointSize(16)
    historytextbox.setFont(textfont)

    testtexting = QTextEdit()

    exampic = QLabel()
    exampic.setScaledContents(True)
    exampic.installEventFilter(None)
    exampic.setMaximumSize(700,700)

    splitter1 = QSplitter(Qt.Horizontal)
    splitter2 = QSplitter(Qt.Vertical)

class layout():
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

mainwind = MainWindow()
mainwind.show()
app.exec()