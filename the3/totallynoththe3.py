import string as s
import random as r

def random_little(text):
    text = eval(text)
    part = []

    row_count = len(text)
    column_count = len(text[0])

    rows = [r.randint(2, row_count), r.randint(2, row_count)]
    columns = [r.randint(2, column_count), r.randint(2, column_count)]

    rows = sorted(rows)
    columns = sorted(columns)
    rotation = r.randint(0,3)

    print(rows,columns,rotation)

    for i in range(rows[0],rows[1]):
        part.append(text[i][columns[0]:columns[1]])

    degree_90 = list(zip(*part[::-1]))
    for row in range(len(degree_90)):
        degree_90[row] = "".join(degree_90[row])

    degree_180 = list(zip(*degree_90[::-1]))
    for row in range(len(degree_180)):
        degree_180[row] = "".join(degree_180[row])

    degree_270 = list(zip(*degree_180[::-1]))
    for row in range(len(degree_270)):
        degree_270[row] = "".join(degree_270[row])

    all_degrees = [part,degree_90,degree_180,degree_270]
    return all_degrees[rotation]


def boom(total): 
    count = 0
    f = open("test_patterns", "a")
    while count < total:
        p1 = random_little(test_i)
        if len(p1) > 2 and len(p1[0]) > 2:
            f.write(str(p1)+"\n")
            count += 1
    f.close()


def random_arrayizer(rows, columns):
    array = []
    letters = s.ascii_letters
    for z in range(rows):
        result_str = ''.join(r.choice(letters) for i in range(columns))
        array.append(result_str)
    f = open("test_images" ,"a")
    f.write(str(array)+"\n")
    f.close()

    g = open("zorttiri","w")
    g.write(str(array))
    g.close()

for i in range(5):
    random_arrayizer(r.randint(20,40),r.randint(20,40))
    f = open("zorttiri")
    test_i = f.read()
    f.close()
    boom(20)