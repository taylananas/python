import tkinter as tk
import customtkinter as ctk
import ctypes

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
width = screensize[0]
height = screensize[1]


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{int(width*0.405)}x{int(height*0.615)}")
        self.title("Ortalama app")

        topFrame = ctk.CTkFrame(master=self)
        topFrame.grid(row=0,column=0)

        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()

        self.quizLabel = ctk.CTkLabel(master=topFrame,text="Quiz Ortalama")
        self.quizLabel.grid(row=0,column=0)

        self.quizMean = ctk.CTkEntry(master=topFrame)
        self.quizMean.grid(row=1,column=0)

        self.midTermLabel = ctk.CTkLabel(master=topFrame,text="Mid-Term Ortalama")
        self.midTermLabel.grid(row=2,column=0)

        self.midTermMean = ctk.CTkEntry(master=topFrame)
        self.midTermMean.grid(row=3,column=0)

        self.opSaWpLabel = ctk.CTkLabel(master=topFrame,text="OP + SA + WP")
        self.opSaWpLabel.grid(row=4,column=0)

        self.opSaWpMean = ctk.CTkEntry(master=topFrame)
        self.opSaWpMean.grid(row=5,column=0)

        self.calculateButton = ctk.CTkButton(master=topFrame,text="Calculate",command=self.hesapla)
        self.calculateButton.grid(row=6,column=0)

        self.ortalamaLabel = ctk.CTkLabel(master=topFrame,text="Ortalama")
        self.ortalamaLabel.grid(row=5,column=1)

        self.ortalama= ctk.CTkEntry(master=topFrame)
        self.ortalama.grid(row=6,column=1)

    def hesapla(self):
        self.var1 = self.quizMean.get()
        self.var2 = self.midTermMean.get()
        self.var3 = self.opSaWpMean.get()

        ortalamavalue = self.var1*0.1

app = App()
app.mainloop()
