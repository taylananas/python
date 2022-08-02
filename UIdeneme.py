import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import customtkinter as ct
from guiGenerator import functs



ct.set_appearance_mode("Light")                  #Genel tema seçenekleri : "Dark","Light","System"
ct.set_default_color_theme("blue")               #Widget renk seçenekleri : "blue", "green", "dark-blue"

class App(ct.CTk):
    
    width = 1000
    height = 750

    

    def __init__(self):
        super().__init__()

        self.title("MyShare")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False,False)
        self.buttonfont = font.Font(family="Helvetica",size=20)
        functs.startUI(self)


if __name__ == "__main__":
    window = App()
    window.mainloop()