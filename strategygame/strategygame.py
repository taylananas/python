from tkinter import *

main=Tk()

main.geometry("600x400")
sp = Button(main,text="Singleplayer",width=12,height=5)
mp = Button(main,text="Multiplayer",width=12,height=5)
sp.place(relx=0.5,rely=0.3,anchor=CENTER)
mp.place(relx=0.5,rely=0.7,anchor=CENTER)


main.mainloop()