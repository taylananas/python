from itertools import count
import random

genomes = [("a","A"),("b","B"),("c","C"),("d","D"),("e","E"),("f","F")]
letters = ["a","b","c","d","e","f","A","B","C","D","E","F"]

counts = {}
probability = 0.01
rangef=20
recur = 0

def genomeselect():
    genno = random.randint(0,1)
    return genno


def genselection():
    genelist = []
    for i in genomes:
        genelist.append(i[genomeselect()])
    return genelist

totallist=[]

for k in range(1000):
    chromosome = genselection()
    totallist.append(chromosome)



def next_generation(mainlist,rangefunc):
    totallist2 = []
    for z in mainlist:
        newchro = []
        for i in z:
            if i.islower():
                k = random.random()
                if k > probability:
                    newchro.append(i)
                else:
                    newchro.append(i.upper())
            else:
                newchro.append(i)
        totallist2.append(newchro)
    counting(totallist2)
    
    return next_generation(totallist2)
    
def counting(liste):
    for k in letters:
        x = 0
        for i in liste:
            z = i.count(k)
            if z:
                x += 1
            counts[k] = x
    print(counts)

while recur < rangef:
    next_generation(totallist)


