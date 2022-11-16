import random
import time
import sys
swords = []
class Sword:
    def __init__(self,name,damage):
        self.name = name
        self.damage = damage
        swords.append(self)

moomoo = Sword('MooMoo', 15)
chad = Sword('Chad', 16)
idle = Sword('IDLE', 17)
bananword = Sword('Bananword', 18)
chunchun = Sword('Chunchunmaru', 19)
lim = Sword('Limlim', 20)
abay = Sword('ABAY',21)
nisnis = Sword('Nisnis',22)
def sword_chooser1():
    global mySword,opSword
    mySword = random.choice(swords)
    opSword = random.choice(swords)
    print(f'YOU| Sword: {mySword.name} | Damage: {mySword.damage}')
    print(f'OP| Sword: {opSword.name} | Damage: {opSword.damage}')

def sword_chooser2():
    global mySword,opSword
    mySword = random.choice(swords)
    opSword = random.choice(swords)
    print(f'P1| Sword: {mySword.name} | Damage: {mySword.damage}')
    print(f'P2| Sword: {opSword.name} | Damage: {opSword.damage}')

def action1():
    while True:
        sword_chooser1()
        if mySword.damage > opSword.damage:
            time.sleep(2)
            print('EZ 1!')
            time.sleep(2)
            while True:
                sword_chooser1()
                time.sleep(2)
                if mySword.damage > opSword.damage:
                    time.sleep(2)
                    print('EZ 2!')
                    time.sleep(2)
                    while True:
                        sword_chooser1()
                        time.sleep(2)
                        if mySword.damage > opSword.damage:          
                            print('EZ 3!')
                            sys.exit('YOU WIN CHAMP!')
                        elif mySword.damage < opSword.damage:                            
                            sys.exit('YOU DIED')
                        elif mySword.damage == opSword.damage:                            
                            print('Draw... AGAIN!!')
                            continue

                elif mySword.damage < opSword.damage:
                    sys.exit('YOU DIED')
                else:
                    print('Draw... AGAIN!!')
                    continue
        elif mySword.damage < opSword.damage:
            time.sleep(2)
            print('YOU DIED!')
            break
        elif mySword.damage == opSword.damage:
            time.sleep(2)
            print('Draw... AGAIN!!')
            time.sleep(2)
            continue
    
def action2():
    while True:
        sword_chooser2()
        time.sleep(2)
        if mySword.damage > opSword.damage:
            print('P1 WINS!')
            c = input('Again? y/n: ')
            if c == 'y':
                continue
            else:
                sys.exit('...')
        elif mySword.damage < opSword.damage:
            print('P2 WINS!')
            c = input('Again? y/n: ')
            if c == 'y':
                continue
            else:
                sys.exit('...')
        elif mySword.damage == opSword.damage:
            print('Draw... AGAIN!!')
            continue

def action3(): #p1vsp2 p1vsp3 p2vsp3
    while True:
        p1,p2,p3 = 0,0,0
        p1n = input('P1 Name: ')
        p2n = input('P2 Name: ')
        p3n = input('P3 Name: ')
        print(f'{p1n} vs {p2n}')
        time.sleep(2)
        while True: #p1vsp2
            p1Sword = random.choice(swords)
            p2Sword = random.choice(swords)
            print(f'{p1n}| Sword: {p1Sword.name} | Damage: {p1Sword.damage}')
            print(f'{p2n}| Sword: {p2Sword.name} | Damage: {p2Sword.damage}')
            time.sleep(2)
            if p1Sword.damage > p2Sword.damage:
                p1 += 1
                print(f'{p1n} WINS')
                break
            elif p1Sword.damage < p2Sword.damage:
                p2 += 1
                print(f'{p2n} WINS')
                break
            else:
                print('Draw... AGAIN!!')
                continue
        time.sleep(2)
        while True: #p2vsp3
            print(f'{p2n} vs {p3n}')
            time.sleep(2)
            p2Sword = random.choice(swords)
            p3Sword = random.choice(swords)
            print(f'{p2n}| Sword: {p2Sword.name} | Damage: {p2Sword.damage}')
            print(f'{p3n}| Sword: {p3Sword.name} | Damage: {p3Sword.damage}')
            time.sleep(2)
            if p2Sword.damage > p3Sword.damage:
                p2 += 1
                print(f'{p2n} WINS')
                break
            elif p2Sword.damage < p3Sword.damage:
                p3 += 1
                print(f'{p3n} WINS')
                break
            else:
                print('Draw... AGAIN!!')
                continue
        time.sleep(2)
        while True: #p1vsp3
            print(f'{p1n} vs {p3n}')
            time.sleep(2)
            p1Sword = random.choice(swords)
            p3Sword = random.choice(swords)
            print(f'{p1n}| Sword: {p1Sword.name} | Damage: {p1Sword.damage}')
            print(f'{p3n}| Sword: {p3Sword.name} | Damage: {p3Sword.damage}')
            time.sleep(2)
            if p1Sword.damage > p3Sword.damage:
                p1 += 1
                print(f'{p1n} WINS')
                break
            elif p1Sword.damage < p3Sword.damage:
                p3 += 1
                print(f'{p3n} WINS')
                break
            else:
                print('Draw... AGAIN!!')
                continue
        time.sleep(2)
        print(f'{p1n}| {p1}')
        print(f'{p2n}| {p2}')
        print(f'{p3n}| {p3}')
        time.sleep(2)
        if p1 == 2:
            print(f'{p1n} CHAMP')
            break
        elif p2 == 2:
            print(f'{p2} CHAMP')
            break
        elif p3 == 2:
            print(f'{p3n} CHAMP')
            break
        elif p1 == 1 and p2 == 1 and p3 == 1:
            continue

def action4(): #p1,p2,p3,p4
    p1 = input('P1 Name: ')
    p2 = input('P2 Name: ')
    p3 = input('P3 Name: ')
    p4 = input('P4 Name: ')
    players = [p1,p2,p3,p4]
    winners = []
    random.shuffle(players)
    print('ROUND 1')
    time.sleep(2)
    print(f'{players[0]} vs {players[1]}')
    time.sleep(2)
    while True:
        s1 = random.choice(swords)
        s2 = random.choice(swords)
        print(f'{players[0]}| Sword: {s1.name} Damage: {s1.damage}')
        print(f'{players[1]}| Sword: {s2.name} Damage: {s2.damage}')
        time.sleep(2)
        if s1.damage > s2.damage:
            print(f'{players[0]} WINS!')
            winners.append(players[0])
            break
        elif s1.damage < s2.damage:
            print(f'{players[1]} WINS!')
            winners.append(players[1])
            break
        else:
            print('Draw.. AGAIN!!')
            time.sleep(2)
            continue
    time.sleep(2)
    print(f'{players[2]} vs {players[3]}')
    time.sleep(2)
    while True:
        s1 = random.choice(swords)
        s2 = random.choice(swords)
        print(f'{players[2]}| Sword: {s1.name} Damage: {s1.damage}')
        print(f'{players[3]}| Sword: {s2.name} Damage: {s2.damage}')
        time.sleep(2)
        if s1.damage > s2.damage:
            print(f'{players[2]} WINS!')
            winners.append(players[2])
            break
        elif s1.damage < s2.damage:
            print(f'{players[3]} WINS!')
            winners.append(players[3])
            break
        else:
            print('Draw.. AGAIN!!')
            time.sleep(2)
            continue 
    time.sleep(2)
    print('FINAL ROUND!')
    time.sleep(2)
    print(f'{winners[0]} vs {winners[1]}')
    time.sleep(2)
    while True:
        s1 = random.choice(swords)
        s2 = random.choice(swords)
        print(f'{winners[0]}| Sword: {s1.name} Damage: {s1.damage}')
        print(f'{winners[1]}| Sword: {s2.name} Damage: {s2.damage}')
        time.sleep(2)
        if s1.damage > s2.damage:
            print(f'EZ! {winners[0]} CHAMP!')
            break
        elif s1.damage < s2.damage:
            print(f'EZ! {winners[1]} CHAMP!')
            break
        else:
            print('Draw... AGAIN!!')
            time.sleep(2)
            continue
            



def compute():
    p = int(input('Player: '))
    if p == 1:
        action1()
    elif p == 2:
        action2()
    elif p == 3:
        action3()
    elif p == 4:
        action4()
    else:
        raise ValueError('Invalid mod.')

if __name__ == '__main__':
    compute()