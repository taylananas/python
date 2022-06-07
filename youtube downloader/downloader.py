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

        self.filePathText = tk.Entry(master=topFrame,disabledforeground = "silver",width = 70,state="normal",disabledbackground="#333333")
        self.filePathText.grid(row=3,column=0,columnspan=2)
        self.filePathText.insert(0,"Filepath for downloaded videos"); self.filePathText.config(state="disabled")

        filePathButton = customtkinter.CTkButton(master=topFrame,text="Set File Path",command=self.selectFilePath)
        filePathButton.grid(row=3,column=2)

        #top right frame// video selection ,url insert etc.
        self.resValue= tk.IntVar(value=0)

        customtkinter.CTkLabel(master=topFrame,text="").grid(row=1,rowspan=1,column=3,columnspan=2)
        customtkinter.CTkLabel(master=topFrame,text="URL",height=42).grid(row=0,column=3,columnspan=2)


        self.urlText = tk.Entry(master=topFrame,bg = "#333333",fg = "silver",width = 97)
        self.urlText.grid(row=2,column=3,columnspan=2)
        searchButton = customtkinter.CTkButton(master=topFrame,text="Select Video",command=self.selectVideo).grid(row=3,column=3)

        self.videoLabel = customtkinter.CTkLabel(master=topFrame,text="")
        self.videoLabel.grid(row=4,column=3,columnspan=2)

        self.p144RadioButton = customtkinter.CTkRadioButton(value=17,master=topFrame,text="144p         ",state="disabled",variable = self.resValue)
        self.p144RadioButton.grid(row=5,column=3,columnspan=2)

        self.p240RadioButton = customtkinter.CTkRadioButton(value=133,master=topFrame,text="240p         ",state="disabled",variable = self.resValue)
        self.p240RadioButton.grid(row=6,column=3,columnspan=2)

        self.p360RadioButton = customtkinter.CTkRadioButton(master=topFrame,value=18,text="360p         ",state="disabled",variable = self.resValue)
        self.p360RadioButton.grid(row=7,column=3,columnspan=2)

        self.p480RadioButton = customtkinter.CTkRadioButton(master=topFrame,value=135,text="480p         ",state="disabled",variable = self.resValue)
        self.p480RadioButton.grid(row=8,column=3,columnspan=2)

        self.p72030RadioButton = customtkinter.CTkRadioButton(master=topFrame,value=22,text="720p/30f  ",state="disabled",variable = self.resValue)
        self.p72030RadioButton.grid(row=9,column=3,columnspan=2)

        self.p72060RadioButton = customtkinter.CTkRadioButton(master=topFrame,value=298,text="720p/60f  ",state="disabled",variable = self.resValue)
        self.p72060RadioButton.grid(row=10,column=3,columnspan=2)

        self.p1080RadioButton = customtkinter.CTkRadioButton(master=topFrame,value=299,text="1080p/60f",state="disabled",variable = self.resValue)
        self.p1080RadioButton.grid(row=11,column=3,columnspan=2)

        """
        17-144p
        133-240p
        18-360p
        135-480p
        22-720p/30f
        298-720p/60f
        299-1080p/60f
        """

        self.downloadButton = customtkinter.CTkButton(master=topFrame,text="Download Video",state="disabled")
        self.downloadButton.grid(row=3,column=4)

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

        self.p144RadioButton.configure(state="disabled")
        self.p240RadioButton.configure(state="disabled")
        self.p360RadioButton.configure(state="disabled")
        self.p480RadioButton.configure(state="disabled")
        self.p72030RadioButton.configure(state="disabled")
        self.p72060RadioButton.configure(state="disabled")
        self.p1080RadioButton.configure(state="disabled")

        for i in ytvideo.streams:
            if i.itag == 17:
                self.p144RadioButton.configure(state="normal")
            elif i.itag == 133:
                self.p240RadioButton.configure(state="normal")
            elif i.itag == 18:
                self.p360RadioButton.configure(state="normal")
            elif i.itag == 135:
                self.p480RadioButton.configure(state="normal")
            elif i.itag == 22:
                self.p72030RadioButton.configure(state="normal")
            elif i.itag == 298:
                self.p72060RadioButton.configure(state="normal")
            elif i.itag == 299:
                self.p1080RadioButton.configure(state="normal")

    def downloadVideo(self):
        self.itagValue = self.resValue.get()
        self.filePath = self.filename
        self.stream = ytvideo.streams.get_by_itag(self.resValue.get())
        stream.download(output_path=self.filePath)

app = App()
app.mainloop()
