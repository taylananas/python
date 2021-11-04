from numpy import *

control = True

def populationsim(R, startpop):
    while control == True:   
        pop = 1
        oldpop = pop
        pop = round((startpop * R))
        if oldpop == pop:
            control = False
        print(pop)
