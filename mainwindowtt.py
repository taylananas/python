from PySide6.QtWidgets import QApplication, QFrame, QGridLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QDialog
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
    
        frameLayout = QGridLayout()
        frameLayout.addWidget(mainbuttonsframe,0,0)
        
        mainframe = QWidget()
        mainframe.setLayout(frameLayout)

        self.setCentralWidget(mainframe)

app = QApplication(sys.argv)


class fucktions():
    def printer():
        print("Hi")

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

class sliders():
    pass


window = Window()
window.show()
app.exec()
