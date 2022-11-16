import random
import string
import time
password = 'Dc]h'
aaa = string.ascii_letters + string.digits + string.punctuation
x = 1
current = time.time()
while True:
    r = random.sample(aaa, k = 4)
    a = ''.join(r)
    if x%100000 == 0:
        current2 = time.time()
        print(f'{x}| {a} | {current2 - current}')
    x += 1
    if a == password:
        current2 = time.time()
        print(f'CUMCUCMUCMCUMCUCM | {x} | {current2 - current}')
        break