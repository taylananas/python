import random

start_money = 100000
month = 0
money = start_money
def nextmonth():
    risk = random.random()*4
    money = money*risk
    print(money)

for i in range(10):
    nextmonth()