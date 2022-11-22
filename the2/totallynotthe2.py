#case1

a=[(12.5,11.3), (2.0,12.0), (18.7,16.2), (12.5,7.0)] #test for case1

case1 = [(7,8), (9,10), (13,4), (4,6)]
case2 = [(7,5), (3,4), (5,7), (8,9)]
case3 = [(12,16), (7,3), (6,2), (4,8)]
case4 = [(11,12), (17,4), (7,8), (13,16)]
case4inv = [(11,16), (17,8), (7,4), (13,12)]
case3right = [(13,2), (4.0,5), (9,6), (4,12)]
casenegative = [(-4,8), (8,12), (7,9), (-3,4)]
test1 = [(57,28), (12,33), (48,77), (51,67)]
# [(8,8), (4,2), (6,6), (3,7)]
# [(10,-14), (6,-20), (8,-16), (5,-15)]



def area(string):
    negcheck = 0
    vexes = string
    vexes = vexes[2:-2]
    listvexs = vexes.split("), (")
    listvexs[0] = listvexs[0].split(",")
    listvexs[1] = listvexs[1].split(",")
    listvexs[2] = listvexs[2].split(",")
    listvexs[3] = listvexs[3].split(",")
    listvexs[0][0] = float(listvexs[0][0])
    listvexs[0][1] = float(listvexs[0][1])
    listvexs[1][0] = float(listvexs[1][0])
    listvexs[1][1] = float(listvexs[1][1])
    listvexs[2][0] = float(listvexs[2][0])
    listvexs[2][1] = float(listvexs[2][1])
    listvexs[3][0] = float(listvexs[3][0])
    listvexs[3][1] = float(listvexs[3][1])
    if listvexs[0][1] < 0 or listvexs[1][1] < 0 or listvexs[2][1] < 0 or listvexs[3][1] < 0 :
            listvexs[0][0] = float(listvexs[0][0])
            listvexs[0][1] = abs(float(listvexs[0][1]))
            listvexs[1][0] = float(listvexs[1][0])
            listvexs[1][1] = abs(float(listvexs[1][1]))
            listvexs[2][0] = float(listvexs[2][0])
            listvexs[2][1] = abs(float(listvexs[2][1]))
            listvexs[3][0] = float(listvexs[3][0])
            listvexs[3][1] = abs(float(listvexs[3][1]))
            negcheck = 1

    alan = 0
    vex = listvexs
    vex2 = sorted(vex)
    
    if negcheck==0:
        if vex[0]==vex2[0]:
            vex=vex
        elif vex[1]==vex2[0]:
            vex = vex[1:]+vex[:1]
        elif vex[2]==vex2[0]:
            vex = vex[2:]+vex[:2]
        elif vex[3]==vex2[0]:
            vex = vex[3:]+vex[:3]
    elif negcheck==1:
        vex = vex[::-1]
        if vex[0]==vex2[0]:
            vex=vex
        elif vex[1]==vex2[0]:
            vex = vex[1:]+vex[:1]
        elif vex[2]==vex2[0]:
            vex = vex[2:]+vex[:2]
        elif vex[3]==vex2[0]:
            vex = vex[3:]+vex[:3]

    print(vex)
    print(vex2)
    
    areas = []
    lenghts = []
    a = ((abs(vex[0][0]-vex[1][0])**2)+(abs(vex[0][1]-vex[1][1])**2))**(1/2)
    b = ((abs(vex[1][0]-vex[2][0])**2)+(abs(vex[1][1]-vex[2][1])**2))**(1/2)
    c = ((abs(vex[2][0]-vex[3][0])**2)+(abs(vex[2][1]-vex[3][1])**2))**(1/2)
    d = ((abs(vex[3][0]-vex[0][0])**2)+(abs(vex[3][1]-vex[0][1])**2))**(1/2)
    e1 = ((abs(vex[0][0]-vex[2][0])**2)+(abs(vex[0][1]-vex[2][1])**2))**(1/2)
    e2 = ((abs(vex[1][0]-vex[3][0])**2)+(abs(vex[1][1]-vex[3][1])**2))**(1/2)

    lenghts.append(a)
    lenghts.append(b)
    lenghts.append(c)
    lenghts.append(d)
    lenghts.append(e1)
    lenghts.append(e2)
    a1 = (vex[0][1]+vex[1][1])*abs(vex[0][0]-vex[1][0])/2
    a2= (vex[1][1]+vex[2][1])*abs(vex[1][0]-vex[2][0])/2
    a3= (vex[2][1]+vex[3][1])*abs(vex[2][0]-vex[3][0])/2
    a4= (vex[3][1]+vex[0][1])*abs(vex[3][0]-vex[0][0])/2

    areas.append(a1)
    areas.append(a2)
    areas.append(a3)
    areas.append(a4)

    if vex[3] == vex2[3]:
        print("Case 1")
        alan = a4

    if vex[2]==vex2[3]:
        print("Case2")
        alan = a4 + a3

    if vex[1]==vex2[3]:
        print("case3")
        if vex[2][0]==vex[3][0]:
            print("middle case")
            alan = a4+a2
        elif vex[2][0]==vex2[2][0]:
            print("Normal Case 2")
            alan = a2+a3+a4
        elif vex[2][1]<vex[3][1]:
            print("Right arrow case")
            s1 = (e2+a+d)/2
            s2 = (e2+b+c)/2
            tri1 = (s1*(s1-a)*(s1-e2)*(s1-d))**(1/2)
            tri2 = (s2*(s2-b)*(s2-e2)*(s2-c))**(1/2)
            alan = a1-(tri1+tri2)
        elif vex[2][1]>vex[3][1]:
            print("Left arrow case")
            s1 = (e1+a+b)/2
            s2 = (e1+d+c)/2
            tri1 = (s1*(s1-a)*(s1-b)*(s1-e1))**(1/2)
            tri2 = (s2*(s2-c)*(s2-d)*(s2-e1))**(1/2)
            alan = a1-(tri1+tri2)


    alan = "%.4f"%alan 
    alan = float(str(alan[:-2]))
    alan = "%.2f"%alan
    print(string,alan)

def areaformatter():
    vexs = []
    for i in range(8):
        vexs.append(input())

    string = f"[({vexs[0]},{vexs[1]}), ({vexs[2]},{vexs[3]}), ({vexs[4]},{vexs[5]}), ({vexs[6]},{vexs[7]})]"
    print(string)
    return string
f = open("cases.txt")
temp = f.read().splitlines()
for i in temp:
    area(i)


