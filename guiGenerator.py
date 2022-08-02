import customtkinter as ct
from tkinter import ttk
import tkinter as tk
class functs():
    def startUI(self):
            # Frames ------------------

            self.main_frame = ct.CTkFrame(self,width=950,height=700)
            self.main_frame.grid(padx=25,pady=20)
            self.main_frame.grid_propagate(0)

            self.button_frame = ct.CTkFrame(self.main_frame,width=900,height=60)
            self.button_frame.grid_columnconfigure(0,minsize=100)
            self.button_frame.grid_columnconfigure(6,minsize=100)
            self.button_frame.grid_columnconfigure(2,weight=1)
            self.button_frame.grid_columnconfigure(4,weight=1)
            self.button_frame.grid_propagate(0)
            self.button_frame.grid(row=0,column=0,padx=25,pady=20)

            self.other_frame = ct.CTkFrame(self.main_frame,width=900,height=570)
            self.other_frame.grid(row=1,column=0,padx=25,pady=10)
            self.other_frame.grid_propagate(0)
            

            # Buttons ------------------

            self.button1 = ct.CTkButton(self.button_frame,text="Button1",command=lambda : functs.func1(self),width=200,text_font=("Helvetica",12))
            self.button1.grid(row=0,column=1,pady=15)

            self.button2 = ct.CTkButton(self.button_frame,text="Button2",command=lambda : functs.func2(self),width=200,text_font=("Helvetica",12))
            self.button2.grid(row=0,column=3,pady=15)

            self.button3 = ct.CTkButton(self.button_frame,text="Button3",width=200,text_font=("Helvetica",12))
            self.button3.grid(row=0,column=5,pady=15)
        
    def func1(self):
        state=0
        if state == 1:      # self.state=1 ise yani 1. butonun çıkardığı sayfa açıksa butona tekrar tıklayınca sayfanın bir daha açılmasını engeller.
            pass
        else:
            self.state = 1       # Bu satırda self.state=1 oluyor ve 1. butonun açtığı sayfanın açık olduğunu hafızaya atıyoruz. 1. butona bir daha tıklayınca bir şey olmayacak.
            functs.frameclean(self)
            self.lframe = ct.CTkFrame(self.other_frame,width=410,height=490)
            self.lframe.grid(row=0,column=0,padx=20,pady=20)
            self.lframe.grid_propagate(0)

            self.lframe.grid_columnconfigure(0,weight=1)
            self.lframe.grid_columnconfigure(2,weight=1)

            self.rframe = ct.CTkFrame(self.other_frame,width=410,height=490)
            self.rframe.grid(row=0,column=1,padx=20,pady=20)
            self.rframe.grid_propagate(0)

            self.rframe.grid_columnconfigure(0,weight=1)
            self.rframe.grid_columnconfigure(2,weight=1)

            self.mframe = ct.CTkFrame(self.other_frame,width=150,height=40)
            self.mframe.grid(row=1,column=0,columnspan=2)
            
            

            self.labelframe1 = ct.CTkFrame(self.lframe)
            self.labelframe1.grid(row=0,column=1,pady=20)

            self.label1 = ct.CTkLabel(self.labelframe1,text="Not Selected")
            self.label1.grid()

            self.button1 = ct.CTkButton(self.lframe,text="Select")
            self.button1.grid(row=1,column=1)

            newstyle = ttk.Style()
            newstyle.theme_use("clam")
            newstyle.configure("Treeview",fieldbackground="#c0c2c5")

            columns = ("File","Extension")
            self.table1 =  ttk.Treeview(self.lframe,columns=columns,show='headings',height=20)
            self.table1.column("# 1",width=200)
            self.table1.column("# 2",width=200)
            self.table1.heading("File",text="File")
            self.table1.heading("Extension",text="Extension")
            self.table1.grid(row=2,column=1,pady=30)


            self.labelframe2 = ct.CTkFrame(self.rframe)
            self.labelframe2.grid(row=0,column=1,pady=20)

            self.label2 = ct.CTkLabel(self.labelframe2,text="Not Selected")
            self.label2.grid()

            self.button2 = ct.CTkButton(self.rframe,text="Select")
            self.button2.grid(row=1,column=1)

            newstyle = ttk.Style()
            newstyle.theme_use("clam")
            newstyle.configure("Treeview",fieldbackground="#c0c2c5")

            columns = ("File","Extension")
            self.table2 =  ttk.Treeview(self.rframe,columns=columns,show='headings',height=20)
            self.table2.column("# 1",width=200)
            self.table2.column("# 2",width=200)
            self.table2.heading("File",text="File")
            self.table2.heading("Extension",text="Extension")
            self.table2.grid(row=2,column=1,pady=30)

            self.button3 = ct.CTkButton(self.mframe,text="Match")
            self.button3.grid()

    def func2(self):
        if self.state == 2:
            pass
        else:
            self.state = 2
            functs.frameclean(self)         #Bu kısmı butonların işleyişi daha belli olsun diye yazdım.
            self.label1 = ct.CTkLabel(self.other_frame,text="Merhaba",text_font=("Arial",50))
            self.label1.grid()

    def frameclean(self):
        for i in reversed(self.other_frame.winfo_children()):
            i.destroy()