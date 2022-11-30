#points = [(x1,y1), (x2,y2)]
def slope(points): #finds slope and y intercept
    x1 = points[0][0]
    y1 = points[0][1]
    x2 = points[1][0]
    y2 = points[1][1]

    if x2-x1 > 0.0001:
        slope = (y2-y1)/(x2-x1)
        y_intercept = y1 - slope*x1
        return slope,y_intercept
    else:
        return "Inf"
print(slope([(1.9999,3),(2,4)]))