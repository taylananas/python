def pattern_search(p, i):
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

    for searching_list in all_degrees:
        n = 0
        for row_num in range(len(i)):
            for search in searching_list:
                if search in i[row_num]:
                    n+=1 
                    if n == len(searching_list):
                        index = i[row_num].index(search[0])

                        if all_degrees.index(searching_list) == 0:
                            return((row_num-len(searching_list)+1, index ,0))   

                        elif all_degrees.index(searching_list) == 1:
                            return((row_num-len(searching_list)+1, index ,90))  

                        elif all_degrees.index(searching_list) == 2:
                            return((row_num-len(searching_list)+1, index ,180))  

                        elif all_degrees.index(searching_list) == 3:
                            return((row_num-len(searching_list)+1, index ,270))   
    return False