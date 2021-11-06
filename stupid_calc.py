# (kilo*ayak numarası)/boy(cm)

# def formula(kg,size,cm):
#     p_pass = kg*size/cm
#     return p_pass

# a = int(input("Kilo:"))
# b = int(input("Ayak Numarası:"))
# c = int(input("Boyunuz (cm):"))

# answer = formula(a,b,c)
# answer = round(answer,2)
# print(answer)

from tkinter import *

main = Tk()

def p_passbut():
    main.destroy()

    p_passtk = Tk()
    weight = IntVar()
    height = IntVar()
    footsize = IntVar()
    p_lenght = IntVar()

    def p_formula():
        intweight = weight.get()
        intheight = height.get()
        intfoot = footsize.get()
        answer = intweight*intfoot/intheight
        answer = round(answer,2)
        p_lenght.set(answer)

    Label(p_passtk,text="Weight(kg):").grid(row=0,column=0)
    Entry(p_passtk,textvariable=weight,width=6).grid(row=0,column=1)
    Label(p_passtk,text="Height (cm)").grid(row=1,column=0)
    Entry(p_passtk,textvariable=height,width=6).grid(row=1,column=1)
    Label(p_passtk,text="Foot Size(eu)").grid(row=2,column=0)
    Entry(p_passtk,textvariable=footsize,width=6).grid(row=2,column=1)
    Button(p_passtk,text="Calculate ur p size",command=p_formula).grid(row=3,column=0,columnspan=2)
    Label(p_passtk,text="P Length(cm)").grid(row=4,column=0)
    Entry(p_passtk,textvariable=p_lenght,width=6,state="disabled").grid(row=4,column=1)
    p_passtk.mainloop()

p_passbutton = Button(main,text="P_Pass",command=p_passbut).grid(row=0,column=0)


main.mainloop()