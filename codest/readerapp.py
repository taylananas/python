from msilib.schema import Font
from PySide6.QtWidgets import QApplication, QFrame, QGridLayout, QMainWindow, QTabWidget, QSizePolicy, QPushButton, QWidget, QLineEdit, QDialog, QTextEdit, QFileDialog, QLabel, QSplitter
from PySide6.QtGui import QIcon, QAction, QPixmap, QFont, QMouseEvent
from PySide6.QtCore import *
import sys
from datetime import datetime

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("Reader")
        self.setGeometry(277,60,1366,900)
        self.setCentralWidget(layout.mainframe)
        self.barmenu()

    def barmenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        newFile = fileMenu.addAction("Import File")
        newFile.triggered.connect(functions.imageselection)
        newFile.setShortcut("Ctrl+N")

class functions():
    def imageselection():#selecting that image
        filepath = QFileDialog.getOpenFileName(None, 'Select file', 'c:\\',"Image files (*.jpg *.png *.jfif)")
        pixmap = QPixmap(filepath[0])
        widgets.exampic.setPixmap(pixmap)
        widgets.exampic.show()
        widgets.historytextbox.append(f"{functions.timecurrent()} New image selected at {filepath[0]}")

    def clearvariablelayout(): #clearing a layout
        for i in reversed(range(layout.variableframelayout.count())):
            removedwidget = layout.variableframelayout.itemAt(i).widget()
            removedwidget.setParent(None)
            layout.variableframelayout.removeWidget(removedwidget)
        widgets.historytextbox.append(f"{functions.timecurrent()} New Layout")

    def test1():
        functions.clearvariablelayout()
        layout.variableframelayout.addWidget(widgets.testbut1)
        layout.variableframelayout.addWidget(widgets.testbut3)

    def test2():
        functions.clearvariablelayout()
        layout.variableframelayout.addWidget(widgets.testbut2)

    def timecurrent(): #returns current time
        now = datetime.now().strftime("%H:%M:%S")
        return now

class widgets():
    button1 = QPushButton("1")
    button2 = QPushButton("2")
    button3 = QPushButton("3")
    button4 = QPushButton("4")
    button5 = QPushButton("5")
    button6 = QPushButton("6")

    testlabel = QLabel("TEST")

    testbut1 = QPushButton("test 1")
    testbut2 = QPushButton("test 2")
    testbut3 = QPushButton("test 3")

    button1.setFixedSize(80,80)
    button2.setFixedSize(80,80)
    button3.setFixedSize(80,80)
    button4.setFixedSize(80,80)
    button5.setFixedSize(80,80)
    button6.setFixedSize(80,80)

    button1.clicked.connect(functions.imageselection)
    button2.clicked.connect(functions.test1)
    button3.clicked.connect(functions.test2)

    historytextbox = QTextEdit()
    historytextbox.setReadOnly(True)

    textfont = QFont()
    textfont.setPointSize(12)
    historytextbox.setFont(textfont)

    testtexting = QTextEdit()

    exampic = QLabel()
    exampic.setScaledContents(True)
    exampic.installEventFilter(None)
    exampic.setMaximumSize(1000,600)

    splitter1 = QSplitter(Qt.Horizontal)
    splitter2 = QSplitter(Qt.Vertical)
    splitter2.setMaximumSize(700,700)

class myEvents():
    #clicking on image to create a new window with that image
    widgets.exampic.mousePressEvent = lambda a: print(functions.timecurrent())#FUNCTION HERE

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
    historyframe.setFixedSize(300,400)
    historyframelayout.addWidget(widgets.historytextbox,1,0)
    historyframelayout.addWidget(QLabel("History"),0,0)
    historyframe.setLayout(historyframelayout)

    widgets.splitter2.addWidget(variableframe)
    widgets.splitter2.addWidget(historyframe)

    histvariframe = QFrame()
    histvariframe.setFrameStyle(QFrame.Box | QFrame.Raised)
    histvariframe.setFixedSize(300,600)
    histvarilayout = QGridLayout()
    histvarilayout.addWidget(widgets.splitter2)
    histvariframe.setLayout(histvarilayout)

    imageframe = QFrame()

    tab1 = QTabWidget()
    tab1.addTab(widgets.exampic, "Image")
    tab1.addTab(widgets.testlabel, "Graph")

    imageframe.setFrameStyle(QFrame.Box | QFrame.Raised)
    imageframelayout = QGridLayout()
    imageframelayout.addWidget(tab1)
    imageframe.setLayout(imageframelayout)

    tableframe = QFrame()
    tableframe.setFrameStyle(QFrame.Box | QFrame.Raised)
    tableframelayout = QGridLayout()
    tableframe.setLayout(tableframelayout)
    tableframe.setFixedSize(1366,300)

    widgets.splitter1.addWidget(histvariframe)
    widgets.splitter1.addWidget(imageframe)

    frameLayout = QGridLayout()
    frameLayout.addWidget(mainbuttonsframe,0,0,2,1)
    frameLayout.addWidget(tableframe,2,0,1,3)
    frameLayout.addWidget(widgets.splitter1,0,2,2,1)

    mainframe = QWidget()
    mainframe.setLayout(frameLayout)

mainwind = MainWindow()
mainwind.show()
app.exec()
