import math
import time
import sympy

starttime = time.time()

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

def euler8():
    text = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    split = text.split("0")
    split.sort()
    numbers=[]
    for i in split:
        if len(str(i)) > 13:
            numbers.append(i)
    finalnumbers = []
    for k in numbers:
        x = 0
        while x+13 <= len(k):
            a = k[x:x+13]
            finalnumbers.append(a)
            x += 1
    answers = []
    for i in finalnumbers:
        answer=1
        for b in i:
            answer *= int(b)
            answers.append(answer)
    answers.sort()

def euler10(numberrange):
    primes = []
    def isprime(number):
        for i in range(2,number):
            if number % i == 0:
                return False
        return True
    
    for x in range(2,numberrange):
        if isprime(x):
            primes.append(x)
    
    print(sum(primes))


def euler11():
    f = open("number11.txt")
    linelist = []
    text = f.read().splitlines()
    for i in text:
        linelist.append(i.split(" "))
    for i in linelist: print(i)

def euler12():
    num = pow(2,1000)
    numstr = str(num)
    sum = 0
    for i in numstr:
        sum += int(i)
    print(sum)

def euler13():
    sum = 0
    f = open("number13.txt")
    flist = f.readlines()
    for i in flist:
        sum += int(i)
    print(str(sum)[:10])

euler11()

endtime = time.time()
runtime = endtime-starttime
print(runtime)