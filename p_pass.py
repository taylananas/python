# (kilo*ayak numarası)/boy(cm)

def formula(kg,size,cm):
    p_pass = kg*size/cm
    return p_pass

a = int(input("Kilo:"))
b = int(input("Ayak Numarası:"))
c = int(input("Boyunuz (cm):"))

answer = formula(a,b,c)
answer = round(answer,2)
print(answer)