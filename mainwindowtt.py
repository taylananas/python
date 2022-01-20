from PySide6.QtWidgets import QApplication, QFrame, QGridLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QDialog
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setWindowTitle("Main")

        frameLayout = QGridLayout()
        frameLayout.addWidget(buttons.button1,0,0)
        
        mainframe = QWidget()
        mainframe.setLayout(frameLayout)

        self.setCentralWidget(mainframe)

app = QApplication(sys.argv)


class fucktions():
    def printer():
        print("Hi")

class buttons():
    button1 = QPushButton("Sa")
    button1.clicked.connect(fucktions.printer)

class sliders():
    pass


window = Window()
window.show()
app.exec()
