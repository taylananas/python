import math


def euler9():
    # a + b + c = 1000
    # a^2 + b^2 = c^2
    # a < b < c
    # a.b.c = ?
    for c in range(1,1000):
        for b in range(1,1000-c):
            a = 1000 - (c + b)
            if a**2 + b**2 == c**2 and a<b<c:
                print(a,b,c)
                print(a*b*c)

def euler34():
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
