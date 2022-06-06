import tkinter as tk
import customtkinter
from tkinter import filedialog

from pip import main
import ctypes

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

        topLeftFrame = customtkinter.CTkFrame(master=self)
        topLeftFrame.grid(row=0,column=0)

        topLeftFrame.grid_rowconfigure(9) #layout 10x10
        topLeftFrame.grid_columnconfigure(9)

        self.optionsLabel = customtkinter.CTkLabel(master=topLeftFrame,text="Options")
        self.optionsLabel.grid(row=0,column=0,columnspan=3)

        self.filePathLabel = customtkinter.CTkLabel(master=topLeftFrame,text = "Filepath")
        self.filePathLabel.grid(row=1,column=0,columnspan=3)

        self.filePathText = tk.Text(master=topLeftFrame,bg = "#333333",fg = "silver",height =1,width = 50,state="normal")
        self.filePathText.grid(row=2,column=0,columnspan=2)
        self.filePathText.insert(1.0, "Filepath"); self.filePathText.config(state="disabled")

        filePathButton = customtkinter.CTkButton(master=topLeftFrame,text="Set File Path",command=self.selectFilePath)
        filePathButton.grid(row=2,column=2)

    def selectFilePath(self):
        filename = filedialog.askdirectory()
        self.filePathText.config(state = "normal")
        self.filePathText.delete(1.0,"end")
        self.filePathText.insert(1.0, filename)
        self.filePathText.config(state="disabled")


app = App()
app.mainloop()
