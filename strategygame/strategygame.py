from tkinter import *
import random
from numpy import random as npr

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
    moneyint.set(1000)
    infamount = StringVar()
    cavamount = StringVar()
    artamount = StringVar()
    infamount.set(0)
    cavamount.set(0)
    artamount.set(0)
    armyl = Label(singleplayer,text="Army Overview")
    armyl.grid(row=3,column=1)
    infantry = Label(singleplayer,text="Infantry")
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

    def infbuy():
        if int(moneyint.get()) >= 100:
            infamount.set(str(int(infamount.get())+10))
            moneyint.set(str(int(moneyint.get())-100))
    def cavbuy():
        if int(moneyint.get()) >= 150:
            cavamount.set(str(int(cavamount.get())+5))
            moneyint.set(str(int(moneyint.get())-150))            
    def artbuy():
        if int(moneyint.get()) >= 300:
            artamount.set(str(int(artamount.get())+3))
            moneyint.set(str(int(moneyint.get())-300))


    infbuybut = Button(singleplayer,text="Buy 10x Infantry\nCost 100",command=infbuy)
    infbuybut.grid(row=4,column=3)
    cavbuybut = Button(singleplayer,text="Buy 5x Cavalry\nCost 150",command=cavbuy)
    cavbuybut.grid(row=5,column=3)
    artbuybut = Button(singleplayer,text="Buy 3x Artillery\nCost 300",command=artbuy)
    artbuybut.grid(row=6,column=3)

    def getinf():
        infamt = int(infamount.get())
        return infamt
    def getcav():
        cavamt = int(cavamount.get())
        return cavamt
    def getart():
        artamt = int(artamount.get())
        return artamt

    

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