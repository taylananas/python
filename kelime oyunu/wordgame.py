from PySide6.QtWidgets import QApplication, QFrame, QGridLayout, QMainWindow, QTabWidget, QSizePolicy, QPushButton, QWidget, QLineEdit, QDialog, QTextEdit, QFileDialog, QLabel, QSplitter
from PySide6.QtGui import QIcon, QAction, QPixmap, QFont, QMouseEvent
from PySide6.QtCore import *
from PySide6 import QtCore
import sys

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setGeometry(100,100,1100,600)
        self.setCentralWidget(layout.MainFrame)
class widgets():
    BigFont = QFont()
    BigFont.setPointSize(102)

    MediumFont = QFont()
    MediumFont.setPointSize(25)

    QuestionText = QTextEdit()
    QuestionText.setReadOnly(True)
    QuestionText.setFixedSize(1100,300)


    TimeLeftText = QLabel("Time")
    TimeLeftText.setFont(MediumFont)
    TimeLeftText.setFixedSize(200,100)

    NameText = QLabel("Name")
    NameText.setFont(MediumFont)
    NameText.setFixedSize(200,100)

    TotalPointText = QLabel("Total")
    TotalPointText.setFont(MediumFont)
    TotalPointText.setFixedSize(200,100)

    QuestionPointText = QLabel("Question")
    QuestionPointText.setFont(MediumFont)
    QuestionPointText.setFixedSize(200,100)

    WordText = QLabel("-_ _ _ _ _ _ _ _ _ _-")
    WordText.setAlignment(QtCore.Qt.AlignCenter)
    WordText.adjustSize()
    WordText.setFont(QFont("Ariel",72))
    WordText.setStyleSheet("border: 1px solid black")

    WordText.setFixedSize(880,160)

    StopTimeButton = QPushButton("Stop Time (A)")
    StopTimeButton.setFixedSize(210,100)


    ShowAnswerButton = QPushButton("Show Answer (S)")
    ShowAnswerButton.setFixedSize(210,100)

    NewLetterButton = QPushButton("New Letter (D)")
    NewLetterButton.setFixedSize(210,100)


class functions():
    pass

class layout():
    MainLayout = QGridLayout()
    #row,column,rowspan,columnspan
    MainThreeFrame = QFrame()
    MainThreeFrame.setFrameStyle(QFrame.Box)
    MainThreeFrame.setFixedSize(160,300)
    MainThreeFrameLO = QGridLayout()
    MainThreeFrameLO.addWidget(widgets.TimeLeftText,0,0)
    MainThreeFrameLO.addWidget(widgets.QuestionPointText,1,0)
    MainThreeFrameLO.addWidget(widgets.TotalPointText,2,0)
    MainThreeFrame.setLayout(MainThreeFrameLO)

    BigFourFrame = QFrame()
    BigFourFrame.setFixedSize(880,140)
    BigFourFrame.setFrameStyle(QFrame.Box)
    BigFourFrameLO = QGridLayout()
    BigFourFrameLO.addWidget(widgets.NameText,0,0)
    BigFourFrameLO.addWidget(widgets.StopTimeButton,0,1)
    BigFourFrameLO.addWidget(widgets.ShowAnswerButton,0,2)
    BigFourFrameLO.addWidget(widgets.NewLetterButton,0,3)
    BigFourFrame.setLayout(BigFourFrameLO)

    QPBFrame = QFrame()
    QPBFrame.setFixedSize(890,320)
#   QPBFrame.setFrameStyle(QFrame.Box | QFrame.Raised)
    QPBFrameLO = QGridLayout()
    QPBFrameLO.addWidget(widgets.WordText,1,0)
    QPBFrameLO.addWidget(BigFourFrame,0,0)
    QPBFrame.setLayout(QPBFrameLO)

    MainFrame = QWidget()
    MainLayout.addWidget(MainThreeFrame,0,0)
    MainLayout.addWidget(QPBFrame,0,1)
    MainLayout.addWidget(widgets.QuestionText,1,0,1,0)
    MainFrame.setLayout(MainLayout)

mainwind = MainWindow()
mainwind.show()
app.exec()
