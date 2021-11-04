from numpy import *

def populationsim(R, startpop):
    control = True
    pop = startpop
    oldpop = pop
    while control == True and pop < 1000000:   
        pop = round((pop * R))
        if oldpop == pop:
            control = False
        print(pop)
    return pop
    
randomr = random.uniform(1,2)
print(f"{1}: {randomr}, {populationsim(randomr,5)}")
