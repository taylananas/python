from tkinter import *
from tkinter import filedialog

def main():
    mainwindow = Tk()
    
    def fileselection():
        selected_folder = filedialog.askdirectory()

    frame1 = LabelFrame(mainwindow,padx=20,pady=20).grid(row=0,column=0)
    Button(frame1,text="Select Directory",command=fileselection).grid(row=0,column=0)
    
    mainwindow.mainloop()

if __name__ == '__main__':
    main() 