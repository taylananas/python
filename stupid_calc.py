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

    p_passtk.mainloop()
p_passbutton = Button(main,text="P_Pass",command=p_passbut).grid(row=0,column=0)

main.mainloop()