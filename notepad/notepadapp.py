from PySide6.QtWidgets import QApplication, QFrame, QGridLayout, QMainWindow, QPushButton, QWidget, QLineEdit, QDialog, QTextEdit
from PySide6.QtGui import QIcon, QAction
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setWindowTitle("Notepad")
        self.setGeometry(360,140,1200,800)
        self.setlayout()
        self.setmenu()

    def setmenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")

        newAction = QAction("New",self)
        fileMenu.addAction(newAction)

        saveAction = QAction("Save",self)
        fileMenu.addAction(saveAction)

    def setlayout(self):
        frameLayout = QGridLayout()
        frameLayout.addWidget(widgets.maintextbox,0,0)
        mainframe = QWidget()
        mainframe.setLayout(frameLayout)
        self.setCentralWidget(mainframe)


app = QApplication(sys.argv)

class functions():
    pass

class widgets():
    maintextbox = QTextEdit()

mainwind = Window()
mainwind.show()
app.exec()