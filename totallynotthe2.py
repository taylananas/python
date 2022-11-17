#case1

a=[(12.5,11.3), (2.0,12.0), (18.7,16.2), (12.5,7.0)] #test for case1

case1 = [(7,8),(9,10),(13,4),(4,6)]
case2 = [(7,5),(3,4),(5,7),(8,9)]
case3 = [(12,16),(7,3),(6,2),(4,8)]
case4 = [(11,12),(17,4),(7,8),(13,16)]
case4inv = [(11,16),(17,8),(7,4),(13,12)]
case3right = [(13,2),(4.0,5),(9,6),(4,12)]


def area(vexinput):
    alan = 0
    vex = vexinput
    vex2 = sorted(vex)
    
    
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
        if vex[1] == vex2[1] or vex[1][0] == vex[2][0]:
            print("Case 1")
            alan = a4
        elif vex[1]== vex2[2]:
            ucgenalan = 0
            print("FUCKING APTAL CASE 4")
            if vex[1][1]>vex[2][1]:
                print("Left arrow case 4")
                s = (b+c+e2)/2
                ucgenalan = (vex[1][0]-vex[2][0])/(vex[3][0]-vex[2][0])*(s*(s-b)*(s-e2)*(s-c))**(1/2)
                print(ucgenalan)
                alan = a4 + ucgenalan
            elif vex[1][1]<vex[2][1]:
                print("Right Arrow Case 4")
                s = (b+a+e1)/2
                ucgenalan = (vex[1][0]-vex[2][0])/(vex[1][0]-vex[0][0])*(s*(s-b)*(s-e1)*(s-a))**(1/2)
                print(ucgenalan)
                alan = a4 + ucgenalan

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
        elif vex[3][1]>vex[2][1]:
            print("Left arrow case")
            s1 = (e1+a+b)/2
            s2 = (e1+d+c)/2
            tri1 = (s1*(s1-a)*(s1-b)*(s1-e1))**(1/2)
            tri2 = (s2*(s2-c)*(s2-d)*(s2-e1))**(1/2)
            alan = a1-(tri1+tri2)


    alan = "%.2f"%alan
    print(alan)



area(case3right)