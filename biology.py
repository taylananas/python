import random

genomes = [("a","A"),("b","B"),("c","C"),("d","D")]

def genomeselect():
    genno = random.randint(0,1)
    return genno

class gene():
    def genselection():
        genelist = []
        for i in genomes:
            genelist.append(i[genomeselect()])
        return genelist

totallist=[]

for k in range(100):
    a = gene.genselection()
    totallist.append(a)
