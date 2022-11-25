def testing(inputxt):
    alan=0
    coordinates=eval(inputxt)
    print(coordinates)
    V0=coordinates[0]
    V1=coordinates[1]
    V2=coordinates[2]
    V3=coordinates[3]
    V0X=V0[0]
    V0Y=V0[1]
    V1X=V1[0]
    V1Y=V1[1]
    V2X=V2[0]
    V2Y=V2[1]
    V3X=V3[0]
    V3Y=V3[1]

    a=min(V0X,V1X,V2X,V3X)

    if a==V0X==V1X :
        print("durum 1 falan filan")
        V0=coordinates[0]
        V1=coordinates[1]
        V2=coordinates[2]
        V3=coordinates[3]

    elif a==V1X==V2X :
        print("durum 2")
        V0=coordinates[1]
        V1=coordinates[2]
        V2=coordinates[3]
        V3=coordinates[0]
        
    elif a==V2X==V3X :
        print("durum 3")
        V0=coordinates[2]
        V1=coordinates[3]
        V2=coordinates[0]
        V3=coordinates[1]

    elif a==V3X==V0X :
        print("durum 4")
        V0=coordinates[3]
        V1=coordinates[0]
        V2=coordinates[1]
        V3=coordinates[2]

    elif min(V0X,V1X,V2X,V3X)==V1X :
        print("durum 5")
        V0=coordinates[1]
        V1=coordinates[2]
        V2=coordinates[3]
        V3=coordinates[0]
    elif min(V0X,V1X,V2X,V3X)==V2X :
        print("durum 6")
        V0=coordinates[2]
        V1=coordinates[3]
        V2=coordinates[0]
        V3=coordinates[1]
    elif min(V0X,V1X,V2X,V3X)==V3X :
        print("durum 7")
        V0=coordinates[3]
        V1=coordinates[0]
        V2=coordinates[1]
        V3=coordinates[2]
    else:                           #V0X minimum durumu
        print("durum 8")
        V0=coordinates[0]
        V1=coordinates[1]
        V2=coordinates[2]
        V3=coordinates[3]
    
    print(V0,V1,V2,V3)
    V0X=V0[0]
    V0Y=V0[1]
    V1X=V1[0]
    V1Y=V1[1]
    V2X=V2[0]
    V2Y=V2[1]
    V3X=V3[0]
    V3Y=V3[1]
    print(V0,V1,V2,V3)

    b=max(V0X,V1X,V2X,V3X)

    if b==V1X==V2X :
        print("yes")
        alan=(V0Y+V3Y)/2*(V3X-V0X)+(V3Y+V2Y)/2*(V2X-V3X)

    elif b==V2X==V3X :                          #kare durumu da buraya dahil
        print("yes2")
        alan=(V0Y+V3Y)/2*(V3X-V0X)
    elif max(V0X,V1X,V2X,V3X)==V2X :
        print("yes3")
        alan=(V0Y+V3Y)/2*(V3X-V0X)+(V3Y+V2Y)/2*(V2X-V3X)

    elif max(V0X,V1X,V2X,V3X)==V3X :
        print("yes4")
        alan=(V0Y+V3Y)/2*(V3X-V0X)

    else :                                       #max(V0X,V1X,V2X,V3X)==V1X
        print("yes5")
        alan=(V0Y+V1Y)/2*(V1X-V0X)-((V1X-V3X)*(V2Y-V0Y)-(V2X-V0X)*(V1Y-V3Y))/2
        
    cevap=("%.4f"%alan)
    cevap = str(cevap)[:-2]
    print(cevap)

testing("[(0,0), (8,5), (0,10), (16,5)]")