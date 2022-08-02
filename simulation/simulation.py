import random

def eylem(r, z):
    list = []
    cheatedProb = 0
    b = 1
    for i in range(r): #yarismaci
        a = 0
        cheatedProb = random.uniform(0.5,0.55)
        for k in range(z): #atislar
            prob = random.random()
            if prob < cheatedProb:
                a += 1
        list.append(f"no:{b} wins:{a} cheatincline:{cheatedProb}")
        b += 1
    print(list)

eylem(20,25000)
