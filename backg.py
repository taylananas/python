import os

month = 1
money = 0
inflation = 0
change = 0
farms = 0
while True:
    os.system("cls")
    print(f"""
Money:{money}               Month:{month}
Inflation:{inflation}           Farms:{farms}   
Change:{change}             Income:{farms*50}
    """)
    deger = input("Enter Farms Amount:")
    months = int(input("Months to simulate:"))
    i = 0
    while i < months:
        if deger:
            money1 = money
            money1 = money
            farms += int(deger)
            money += farms*20
            money -= inflation
            money = float("%.2f" % money)
            inflation = float("%.2f" % (inflation + month*10 + money*0.08)) 
            change = money-money1
            change = float("%.2f" % change)
            month += 1
            i+=1
