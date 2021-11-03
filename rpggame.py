from tkinter import *


def main():
    MainWindow = Tk()
    health = IntVar()
    health.set(100)
    healthlabel = Label(MainWindow,text = "health:").grid(row=0,column=0)
    healthentry = Entry(MainWindow,textvariable=health,state="disabled",width=3).grid(row=0,column=1)
    MainWindow.mainloop()

main()