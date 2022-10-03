import os

month = 1
money = 0
inflation = 0
change = 0
while True:
    os.system("clear")
    print(f"Money: {money}")
    print(f"Inflation: {inflation}")
    print(f"Change: {change}")
    print(f"Month: {month}")
    deger = input("Enter Money:")
    if deger:
        money1 = money
        money1 = money
        money += int(deger)
        inflation = money*0.08
        money -= inflation
        money = float("%.2f" % money)
        inflation = float("%.2f" % inflation)
        change = money-money1
        change = float("%.2f" % change)
        month += 1
