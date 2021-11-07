from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
import os
import random as r
import imghdr

def main():
    mainwindow = Tk()
    global selected_folder
    selected_folder = ""
    def fileselection():
        global selected_folder
        selected_folder = filedialog.askdirectory()

    frame1 = LabelFrame(mainwindow,padx=20,pady=20)
    frame1.grid(row=0,column=0)
    bt1 = Button(frame1,text="Select Directory",command=fileselection)
    bt1.grid(row=0,column=0)
    frame2 = LabelFrame(mainwindow,padx=20,pady=20)
    frame2.grid(row=0,column=1)

    def directorylisting(path):
        global listfiles
        listfiles = os.listdir(path)
        global filecount
        filecount = len(listfiles)
        randomnum = r.randint(0,filecount-1)
        randomimage = listfiles[randomnum]
        if imghdr.what(f"{path}/{randomimage}") in ["png","jpg"]:
            global image1
            global imagelabel
            imagelabel = Label()
            try:
                imagelabel.grid_forget()
                image1 = ImageTk.PhotoImage(Image.open(path+"/"+randomimage).resize([800,600]))
                imagelabel = Label(frame2,image=image1)
                imagelabel.grid(row=0,column=0)        
            except:
                image1 = ImageTk.PhotoImage(Image.open(path+"/"+randomimage).resize([800,600]))
                imagelabel = Label(frame2,image=image1)
                imagelabel.grid(row=0,column=0)

    bt2 = Button(frame1,command=lambda:directorylisting(selected_folder),text="Random Image")
    bt2.grid(row=1,column=0)
    
    mainwindow.mainloop()

if __name__ == '__main__':
    main() 