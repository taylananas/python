import math

listi = []

for i in range(3,10**10):
    suma = 0
    for a in str(i):
        suma += math.factorial(int(a))
        if suma == i:
            print(i)
            listi.append(i)
            print(listi,sum(listi))
print(listi,sum(listi))
