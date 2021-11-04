import requests
from bs4 import BeautifulSoup
from tkinter import *

def usdrate():
    urlusd = "https://www.bloomberght.com/doviz/dolar"
    r_usd = requests.get(urlusd)
    soup = BeautifulSoup(r_usd.content, "html.parser")
    selection = soup.find("span", {"class": "downRed"})
    selectionrate = soup.find("span", {"class": "bulk"})
    selectiondate = soup.find("span", {"class": "date"})
    return selection.text, selectionrate.text, selectiondate.text

def eurrate():
    urlusd = "https://www.bloomberght.com/doviz/euro"
    r_usd = requests.get(urlusd)
    soup = BeautifulSoup(r_usd.content, "html.parser")
    selection = soup.find("span", {"class": "downRed"})
    selectionrate = soup.find("span", {"class": "bulk"})
    selectiondate = soup.find("span", {"class": "date"})  
    return selection.text, selectionrate.text, selectiondate.text

main = Tk()

usdtry,eurtry,usddate,eurdate,usrate,eurate = StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()

#usd/try
usdtry.set(usdrate()[0])
usrate.set(usdrate()[1])
usddate.set(usdrate()[2])
Label(main,text="Exchange").grid(row=0,column=0)
Label(main,text="Exchange Rate").grid(row=0,column=1)
Label(main,text="Rate").grid(row=0,column=2)
Label(main,text="Update Date").grid(row=0,column=3)
Label(main,text="USD/TRY").grid(row=1,column=0)
usdentry = Entry(main, textvariable=usdtry,width=8,state="disabled").grid(row=1,column=1)
usdrateper = Entry(main,textvariable=usrate,width=8,state="disabled").grid(row=1,column=2)
usdate = Entry(main,textvariable=usddate,state="disabled",width=20).grid(row=1,column=3)

#eur/try
eurtry.set(eurrate()[0])
eurate.set(eurrate()[1])
eurdate.set(eurrate()[2])
Label(main,text="EUR/TRY").grid(row=2,column=0)
eurentry = Entry(main, textvariable=eurtry,width=8,state="disabled").grid(row=2,column=1)
eurrateper = Entry(main,textvariable=eurate,width=8,state="disabled").grid(row=2,column=2)
eudate = Entry(main,textvariable=eurdate,state="disabled",width=20).grid(row=2,column=3)

def Update():
    eurtry.set(eurrate()[0])
    eurate.set(eurrate()[1])
    eurdate.set(eurrate()[2])
    usdtry.set(usdrate()[0])
    usrate.set(usdrate()[1])
    usddate.set(usdrate()[2])

Button(main,text="Update",command=Update).grid(row=3,column=2)
def Info():
    info = Tk()
    infotext = Label(info,text=
    """
Powered by BloombergHT

This is a basic exchange rate program using BloombergHT exchange rates.
    """)
    def Quit():
        info.destroy()
    Button(info,text="EXIT",command=Quit).grid(row=1,column=0)
    infotext.grid(row=0,column=0)
    info.mainloop()

def Quit():
    main.destroy()

Button(main,text="QUIT",command=Quit).grid(row=3,column=1)
Button(main,text="INFO",command=Info).grid(row=3,column=3)

main.mainloop()