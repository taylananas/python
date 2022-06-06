import tkinter as tk
import customtkinter
from tkinter import filedialog
from pytube import YouTube
from PIL import Image,ImageTk
from urllib.request import urlopen
from pip import main
import ctypes
import datetime

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
width = screensize[0]
height = screensize[1]


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{int(width*0.6)}x{int(height*0.6)}")
        self.title("Youtube Downloader")

        self.grid_columnconfigure(1) #2x2 grid
        self.grid_rowconfigure(1)

        # topLeft frame//options

        topFrame = customtkinter.CTkFrame(master=self)
        topFrame.grid(row=0,column=0)

        topFrame.grid_rowconfigure(9) #layout 10x10
        topFrame.grid_columnconfigure(9)

        self.optionsLabel = customtkinter.CTkLabel(master=topFrame,text="Options",height=35)
        self.optionsLabel.grid(row=0,column=0,columnspan=3)

        self.emptyLabel = customtkinter.CTkLabel(master=topFrame,text="")
        self.emptyLabel.grid(row=1)

        self.filePathLabel = customtkinter.CTkLabel(master=topFrame,text = "Filepath")
        self.filePathLabel.grid(row=2,column=0,columnspan=3)

        self.filePathText = tk.Entry(master=topFrame,disabledforeground = "silver",width = 60,state="normal",disabledbackground="#333333")
        self.filePathText.grid(row=3,column=0,columnspan=2)
        self.filePathText.insert(0,"Filepath for downloaded videos"); self.filePathText.config(state="disabled")

        filePathButton = customtkinter.CTkButton(master=topFrame,text="Set File Path",command=self.selectFilePath)
        filePathButton.grid(row=3,column=2)

        #top right frame// video selection ,url insert etc.


        customtkinter.CTkLabel(master=topFrame,text="").grid(row=1,rowspan=1,column=3)
        customtkinter.CTkLabel(master=topFrame,text="URL",height=42).grid(row=0,column=3)


        self.urlText = tk.Entry(master=topFrame,bg = "#333333",fg = "silver",width = 80)
        self.urlText.grid(row=2,column=3)
        searchButton = customtkinter.CTkButton(master=topFrame,text="Select Video",command=self.selectVideo).grid(row=3,column=3)
        self.videoLabel = customtkinter.CTkLabel(master=topFrame,text="")
        self.videoLabel.grid(row=4,column=3)



    def selectFilePath(self):
        filename = filedialog.askdirectory()
        self.filePathText.config(state = "normal")
        self.filePathText.delete(0,"end")
        self.filePathText.insert(0, filename)
        self.filePathText.config(state="disabled")

    def selectVideo(self):
        urlpaste = self.urlText.get()
        ytvideo = YouTube(urlpaste)
        videoTitle = ytvideo.title
        videoLength = ytvideo.length
        a = datetime.timedelta(seconds=videoLength)
        self.videoLabel.configure(text=f"Video Title= {videoTitle}\n \nVideo Length= {a}")

        print(type(ytvideo.streams))



app = App()
app.mainloop()
