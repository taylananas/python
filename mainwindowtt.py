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
        mainbuttonsframe.setLayout(mainbuttonslayout)

        variableframe = QFrame()
        variableframelayout = QGridLayout()
        variableframelayout.addWidget(buttons.bigbutton)
        variableframe.setLayout(variableframelayout)

        historyframe = QFrame()
        historyframelayout = QGridLayout()
        historyframelayout.addWidget(textboxes.historytextbox)
        historyframelayout.addWidget(textboxes.testtexting)
        historyframe.setLayout(historyframelayout)

        frameLayout = QGridLayout()
        frameLayout.addWidget(mainbuttonsframe,0,0,2,1)
        frameLayout.addWidget(historyframe,1,1)
        frameLayout.addWidget(variableframe,0,1)
        mainframe = QWidget()
        mainframe.setLayout(frameLayout)

        self.setCentralWidget(mainframe)

app = QApplication(sys.argv)


class functions():
    def printer():
        print("Hi")
    
    def textboxeditor():
        text = textboxes.testtexting.toPlainText()
        print(text)
    
    def historyappender():
        text = textboxes.testtexting.toPlainText()
        textboxes.historytextbox.append(text)

class buttons():
    button1 = QPushButton("1")
    button2 = QPushButton("2")
    button3 = QPushButton("3")
    button4 = QPushButton("4")
    button5 = QPushButton("5")
    button6 = QPushButton("6")
    button1.setFixedSize(60,60)
    button2.setFixedSize(60,60)
    button3.setFixedSize(60,60)
    button4.setFixedSize(60,60)
    button5.setFixedSize(60,60)
    button6.setFixedSize(60,60)
    bigbutton = QPushButton("bigbro")
    bigbutton.setFixedSize(300,300)
    button1.clicked.connect(functions.textboxeditor)
    button2.clicked.connect(functions.historyappender)

class sliders():
    pass

class textboxes():
    historytextbox = QTextEdit()
    testtexting = QTextEdit()

window = Window()
window.show()
app.exec()
