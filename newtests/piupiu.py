import random
chars = ['domuz','kedi','fok','kiz','civciv','ahtapot']
invChars = ['iskelet','yildiz','kelebek']
append = chars + invChars
while True:
    c1 = input('1: ')
    c2 = input('2: ')
    c3 = input('3: ')
    if c1 and c2 and c3 in chars:
        r = random.choices(append, weights=[1,1,1,1,1,1,3,2,5], k = 3)
        print(r)
        break
    else:
        print("Error")
        continue
