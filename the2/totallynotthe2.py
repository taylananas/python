def area(string):
    negcheck = 0
    vexes = eval(string) #takes input and converts it into a list with 4 tuples
    listvexs = vexes
    listvexs[0]=list(vexes[0]) #converts tuples to lists
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
    print(f"Normals : {vex}\n Sorted : {vex2}")
    if vex[3][0] == vex2[3][0]:
        print("klasik 1")
        alan = a4
    elif vex[2]==vex2[3]:
        print("klasik 2")
        alan = a4 + a3
    elif vex[1]==vex2[3]:
        if vex[2][0]==vex[3][0]:
            print("this")
            alan = a4+a2
        elif vex[2][0]==vex2[2][0]:
            print("thisnt")
            alan = a2+a3+a4
        elif vex[2][1]<vex[3][1]:
            print("this must")
            s1 = (e2+a+d)/2
            s2 = (e2+b+c)/2
            tri1 = (s1*(s1-a)*(s1-e2)*(s1-d))**(1/2)
            tri2 = (s2*(s2-b)*(s2-e2)*(s2-c))**(1/2)
            alan = a1-(tri1+tri2)
        elif vex[2][1]>vex[3][1]:
            print("this must not")
            s1 = (e1+a+b)/2
            s2 = (e1+d+c)/2
            tri1 = (s1*(s1-a)*(s1-b)*(s1-e1))**(1/2)
            tri2 = (s2*(s2-c)*(s2-d)*(s2-e1))**(1/2)
            alan = a1-(tri1+tri2)

    alan = "%.2f"%alan
    print(alan)

def areaformatter():
    vexs = []
    for i in range(8):
        vexs.append(input())

    string = f"[({vexs[0]},{vexs[1]}), ({vexs[2]},{vexs[3]}), ({vexs[4]},{vexs[5]}), ({vexs[6]},{vexs[7]})]"
    print(string)
    return string

area(areaformatter())


