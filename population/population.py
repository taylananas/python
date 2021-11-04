from numpy import *

population = 2
a = 1
k = 1
def formula(i, pop):
    R_factor = random.uniform(1.25,1.883)
    while pop < 100000:
        temppop = pop
        pop = pop * R_factor
        pop = round(pop)
        i += 1
        if temppop == pop:
            break
    return i,pop,R_factor

for i in range(40):
    print(k, ":", formula(a,population))
    k += 1