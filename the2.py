def testing():
    sum = 0
    num = "258065-5"
    num_part1 = num[:6]
    num_part2 = num[7:]

    sumnum1 = num_part1[1::2]
    if "?" not in num:
        numlist = [int(i) for i in num_part1]
        numlist.append(int(num_part2))

        



    print(numlist)


testing()
