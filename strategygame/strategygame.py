from tkinter import *

main=Tk()

main.geometry("600x400")

def single():
    main.destroy()

    singleplayer = Tk()

    Label().grid(row=0)
    #money
    moneyint = StringVar()
    moneyl = Label(singleplayer,text="Money")
    moneyl.grid(row=1,column=0)
    moneye = Entry(singleplayer,state="disabled",textvariable=moneyint,width=8)
    moneye.grid(row=1,column=1)
    Label().grid(row=2)
    #army
    infamount = StringVar()
    cavamount = StringVar()
    artamount = StringVar()
    armyl = Label(singleplayer,text="Army Overview")
    armyl.grid(row=3,column=1)
    infantry = Label(singleplayer,text="Infantry:")
    infantry.grid(row=4,column=0)
    infantrye = Entry(singleplayer,state="disabled",textvariable=infamount,width=8)
    infantrye.grid(row=4,column=1)
    cavalry = Label(singleplayer,text="Cavalry")
    cavalry.grid(row=5,column=0)
    cavalrye = Entry(singleplayer,state="disabled",textvariable=cavamount,width=8)
    cavalrye.grid(row=5,column=1)
    artillery = Label(singleplayer,text="Artillery")
    artillery.grid(row=6,column=0)
    artillere = Entry(singleplayer,state="disabled",textvariable=artamount,width=8)
    artillere.grid(row=6,column=1)

    singleplayer.mainloop()

def multi():
    main.destroy()
    multiplayer = Tk()

    multiplayer.mainloop()

sp = Button(main,text="Singleplayer",width=12,height=5,command=single)
mp = Button(main,text="Multiplayer",width=12,height=5,command=multi)

sp.place(relx=0.5,rely=0.3,anchor=CENTER)
mp.place(relx=0.5,rely=0.7,anchor=CENTER)

main.mainloop()