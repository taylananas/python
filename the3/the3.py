def pattern_search(p, i):
    degree_90 = list(zip(*p[::-1]))
    for row in range(len(degree_90)): degree_90[row] = "".join(degree_90[row])
    degree_180 = list(zip(*degree_90[::-1]))
    for row in range(len(degree_180)): degree_180[row] = "".join(degree_180[row])
    degree_270 = list(zip(*degree_180[::-1]))
    for row in range(len(degree_270)): degree_270[row] = "".join(degree_270[row])
    all_degrees, totalRow, totalColumn = [p,degree_90,degree_180,degree_270], len(i), len(i[0])
    for zort,selectedDegree in enumerate(all_degrees):
        patternRow, patternColumn  = len(selectedDegree),len(selectedDegree[0])
        for x in range(totalRow-patternRow+1):
            rows = i[x:x+patternRow]
            for y in range(totalColumn-patternColumn+1):
                temp=[]
                for row in rows: temp.append(row[y:y+patternColumn])
                if temp == selectedDegree: return (x,y,zort*90)
    else: return False