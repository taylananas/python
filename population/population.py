from numpy import *

def populationsim(R, startpop):
    i = 1
    control = True
    pop = startpop
    oldpop = pop
    while control == True and pop < 1000000000000000:   
        pop = round((pop * R))
        if oldpop == pop:
            control = False
        i += 1
    return pop,i


for a in range(100):
    randomr = random.uniform(1,2)
    print(f"{a}: {randomr}, {populationsim(randomr,25)}")
