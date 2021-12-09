from tkinter import *
from tkinter import filedialog

def main():
    mainwindow = Tk()
    frame1 = LabelFrame(mainwindow, text="Menü Seçimi")
    frame1.grid(row=0,column=0,columnspan=3)
    def yenimenu():
        frame2 = LabelFrame(mainwindow, text="Menü")
        frame2.grid(row=1,column=0,columnspan=3)
        menulist = selectedfile.readlines()
        def siparis(isim):
            eksr = ekstratxt.get()
            siparisliste.insert(END,f"{isim}\n ----- {eksr}")
            ekstratxt.set("")
        
        def ilerle():
            indx = siparisliste.curselection()
            hazirlananliste.insert(END,siparisliste.get(indx))
            siparisliste.delete(indx)

        def ilerle2():
            indx = hazirlananliste.curselection()
            tamamlananliste.insert(END,hazirlananliste.get(indx))
            hazirlananliste.delete(indx)

        a = 1
        b = 1
        c = 1
        for i in menulist:
            btt = Button(frame2,text=f"Menü {c}: {i}", command= lambda i=i : siparis(i))
            btt.grid(row=a,column=b)
            a +=1
            if a == 5:
                b+=1
                a = 1
            c+=1
        
        frame3 = LabelFrame(mainwindow, text="Siparişler")
        frame3.grid(row=3,column=0)
        frame4 = LabelFrame(mainwindow,text="Hazırlananlar")
        frame4.grid(row=3,column=1)
        frame5 = LabelFrame(mainwindow,text="Tamamlananlar")
        frame5.grid(row=3,column=2)
        frame6 = LabelFrame(mainwindow,text="İsim, Ekstralar")
        frame6.grid(row=2,column=0,columnspan=3)

        siparisliste = Listbox(frame3,width=50)
        siparisliste.grid(row=0,column=0,rowspan=3)

        rightbutton = Button(frame3, text ="--->",command=ilerle)
        rightbutton.grid(row=1,column=2)

        hazirlananliste = Listbox(frame4,width=50)
        hazirlananliste.grid(row=0,column=0,rowspan=3)

        rightbutton2 = Button(frame4, text ="--->",command=ilerle2)
        rightbutton2.grid(row=1,column=2)

        tamamlananliste = Listbox(frame5,width=50)
        tamamlananliste.grid(row=0,column=0,rowspan=3)       
        
        def silmewk():
            indx = tamamlananliste.curselection()
            tamamlananliste.delete(indx)

        silici = Button(frame5, text ="SİL",command=silmewk)
        silici.grid(row=1,column=2) 

        ekstratxt = StringVar()
        ekstra = Entry(frame6, textvariable=ekstratxt)
        ekstra.grid(row=0,column=0)

    def menulist():
        global selectedfile
        selectedfile = filedialog.askopenfile(mode="r")
        global menulist
        bt3 = Button(frame1,text="Menüyü Oluştur",command=yenimenu)
        bt3.grid(row=0,column=1)
    
    bt1 = Button(frame1,text="Menüyü Seçin",command=menulist)
    bt1.grid(row=0,column=0)

    mainwindow.mainloop()

if __name__ == '__main__':
    main()