from PySide6.QtWidgets import QApplication, QFrame, QGridLayout, QMainWindow, QPushButton, QWidget, QLineEdit, QDialog, QTextEdit, QFileDialog, QLabel
from PySide6.QtGui import QIcon, QAction
import os
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

        imageframe = QFrame()
        imageframe.setFrameStyle(QFrame.Box | QFrame.Raised)
        imageframelayout = QGridLayout()
        imageframe.setLayout(imageframelayout)

        frameLayout = QGridLayout()
        frameLayout.addWidget(mainbuttonsframe,0,0,2,1)
        frameLayout.addWidget(historyframe,1,1)
        frameLayout.addWidget(variableframe,0,1)
        mainframe = QWidget()
        mainframe.setLayout(frameLayout)

        self.setCentralWidget(mainframe)

app = QApplication(sys.argv)

class functions():
    pass

class widgets():
    button1 = QPushButton("1")
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
    historytextbox = QTextEdit()
    testtexting = QTextEdit()
    

mainwind = MainWindow()
mainwind.show()
app.exec()