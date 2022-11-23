cases = open("cases.txt")
answers = open("answers.txt")
temp = cases.read().splitlines()
temp2 = answers.read().splitlines()
wrongs = []

"""

HOW TO USE:
WRITE "inputxt" in the input statement's right side
for example if your code is like:

inputvalues = input()

CHANGE THIS AS
inputvalues = inputxt

and instead of printing the answer, return it

for example:

finalanswer = areaofthegreenzone
print(finalanswer)

INSTEAD OF PRINT, WRITE:
return finalanswer

"""
def testing(inputxt):
    negcheck = 0
    vexes = eval(inputxt)
    listvexs = vexes
    listvexs[0]=list(vexes[0])
    listvexs[1]=list(vexes[1])
    listvexs[2]=list(vexes[2])
    listvexs[3]=list(vexes[3])

    if listvexs[0][1] < 0 or listvexs[1][1] < 0 or listvexs[2][1] < 0 or listvexs[3][1] < 0 :
            listvexs[0][1] = abs(float(listvexs[0][1]))
            listvexs[1][1] = abs(float(listvexs[1][1]))
            listvexs[2][1] = abs(float(listvexs[2][1]))
            listvexs[3][1] = abs(float(listvexs[3][1]))
            negcheck = 1

    vex = listvexs
    vex2 = sorted(vex)

    if negcheck==0:
        if vex[1]==vex2[0]:
            vex = vex[1:]+vex[:1]
        elif vex[2]==vex2[0]:
            vex = vex[2:]+vex[:2]
        elif vex[3]==vex2[0]:
            vex = vex[3:]+vex[:3]

    elif negcheck==1:
        vex = vex[::-1]
        if vex[1]==vex2[0]:
            vex = vex[1:]+vex[:1]
        elif vex[2]==vex2[0]:
            vex = vex[2:]+vex[:2]
        elif vex[3]==vex2[0]:
            vex = vex[3:]+vex[:3]

    a = ((abs(vex[0][0]-vex[1][0])**2)+(abs(vex[0][1]-vex[1][1])**2))**(1/2)
    b = ((abs(vex[1][0]-vex[2][0])**2)+(abs(vex[1][1]-vex[2][1])**2))**(1/2)
    c = ((abs(vex[2][0]-vex[3][0])**2)+(abs(vex[2][1]-vex[3][1])**2))**(1/2)
    d = ((abs(vex[3][0]-vex[0][0])**2)+(abs(vex[3][1]-vex[0][1])**2))**(1/2)
    e1 = ((abs(vex[0][0]-vex[2][0])**2)+(abs(vex[0][1]-vex[2][1])**2))**(1/2)
    e2 = ((abs(vex[1][0]-vex[3][0])**2)+(abs(vex[1][1]-vex[3][1])**2))**(1/2)

    a1 = (vex[0][1]+vex[1][1])*abs(vex[0][0]-vex[1][0])/2
    a2= (vex[1][1]+vex[2][1])*abs(vex[1][0]-vex[2][0])/2
    a3= (vex[2][1]+vex[3][1])*abs(vex[2][0]-vex[3][0])/2
    a4= (vex[3][1]+vex[0][1])*abs(vex[3][0]-vex[0][0])/2

    if vex[3] == vex2[3]:
        alan = a4
    if vex[2]==vex2[3]:
        alan = a4 + a3
    if vex[1]==vex2[3]:
        if vex[2][0]==vex[3][0]:
            alan = a4+a2
        elif vex[2][0]==vex2[2][0]:
            alan = a2+a3+a4
        elif vex[2][1]<vex[3][1]:
            s1 = (e2+a+d)/2
            s2 = (e2+b+c)/2
            tri1 = (s1*(s1-a)*(s1-e2)*(s1-d))**(1/2)
            tri2 = (s2*(s2-b)*(s2-e2)*(s2-c))**(1/2)
            alan = a1-(tri1+tri2)
        elif vex[2][1]>vex[3][1]:
            s1 = (e1+a+b)/2
            s2 = (e1+d+c)/2
            tri1 = (s1*(s1-a)*(s1-b)*(s1-e1))**(1/2)
            tri2 = (s2*(s2-c)*(s2-d)*(s2-e1))**(1/2)
            alan = a1-(tri1+tri2)

    alan = "%.4f"%alan 
    alan = float(str(alan[:-2]))
    alan = "%.2f"%alan
    return alan

def grading():
    total = len(temp)
    grade = 0
    for i in range(total):
        if testing(temp[i]) == temp2[i]:
            grade +=1
        else:
            wrongs.append(i+1)
    
    print(f"{grade}/{total}")
    print(f"Wrong questions are: {wrongs}")

grading()

