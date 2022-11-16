from tkinter import Button
from PySide6.QtWidgets import QApplication, QFrame, QGridLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit
import sys


class nextWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("As")
        self.show()

class Buttona(QPushButton):
    def __init__(self,a,b,c):
        super().__init__(a)
        self.clicked.connect(b)
        self.setCheckable(c)
    
    

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("Sa")

        layout = QGridLayout()
        layout.addWidget(Buttona("sa",nextWindow,True),0,0)
        layout.addWidget(Buttona("da",None,False),1,1)

        layout2 = QGridLayout()
        layout2.addWidget(Buttona("sasa",None,False),0,0)
        layout2.addWidget(Buttona("Dadadadada",None,False),1,1)

        frame = QFrame()
        frame.setFrameStyle(QFrame.StyledPanel)
        frame.setLayout(layout)

        frame2 = QFrame()
        frame2.setFrameStyle(QFrame.Box | QFrame.Sunken)
        frame2.setLayout(layout2)

        
        framelayout = QGridLayout()
        framelayout.addWidget(frame,0,0)
        framelayout.addWidget(frame2,1,1)
        
        mainframe = QWidget()
        mainframe.setLayout(framelayout)
        self.setCentralWidget(mainframe)
    

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()