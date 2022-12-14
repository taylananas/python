def pattern_search(p, i): #! ARADA BOSLUK VARSA DA DOGRU SAYIYOR
    degree_90 = list(zip(*p[::-1]))
    for row in range(len(degree_90)):
        degree_90[row] = "".join(degree_90[row])
    degree_180 = list(zip(*degree_90[::-1]))
    for row in range(len(degree_180)):
        degree_180[row] = "".join(degree_180[row])
    degree_270 = list(zip(*degree_180[::-1]))
    for row in range(len(degree_270)):
        degree_270[row] = "".join(degree_270[row])
    all_degrees = [p,degree_90,degree_180,degree_270]
    for degree ,searching_list in enumerate(all_degrees):
        n = 0
        for row_num in range(len(i)):
            for search in searching_list:
                print(search,i[row_num],n)
                if search in i[row_num]: 
                    n += 1
                    if n == len(searching_list):
                        return ((row_num-len(searching_list)+1, i[row_num].index(search[0]) , degree * 90))
                else: 
                    continue
                
    return False

test_i = ["tuz<abcd", 
          ">#sAY#at", 
          "uzyXAAr.", 
          "r,lAXxio", 
          "z#a!yabc", 
          "yazy?zya"]
test_p = ["AXA", "XAY"]

print(pattern_search(test_p,test_i))