from PySide6.QtWidgets import QApplication, QFrame, QGridLayout, QMainWindow, QPushButton, QWidget, QLineEdit, QDialog, QTextEdit
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setWindowTitle("Main")

        mainbuttonslayout = QGridLayout()
        mainbuttonslayout.addWidget(buttons.button1,0,0)
        mainbuttonslayout.addWidget(buttons.button2,1,0)
        mainbuttonslayout.addWidget(buttons.button3,2,0)
        mainbuttonslayout.addWidget(buttons.button4,3,0)
        mainbuttonslayout.addWidget(buttons.button5,4,0)
        mainbuttonslayout.addWidget(buttons.button6,5,0)

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
        historyframelayout.addWidget(textboxes.historytextbox)
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

class buttons():
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

class sliders():
    pass

class textboxes():
    historytextbox = QTextEdit()
    testtexting = QTextEdit()

class imageshowers():
    pass    

window = Window()
window.show()
app.exec()
