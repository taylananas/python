def construct_forest(defs):
    forest = []
    for funct in defs:
        branch =  []
        k = function_validator(funct)
        branch.extend([k[0],k[1],[k[2]],[k[3]]])
        forest.append(branch)
    tobedeleted = []
    for z in forest:
        if "(" in z[2][0] and not "(" in z[3][0]:
            for k in forest:
                if k[0] in z[2][0]:
                    z[2] = k
                    tobedeleted.append(k[0])
        elif "(" in z[3][0] and not "(" in z[2][0]:
            for k in forest:
                if k[0] in z[3][0]:
                    z[3] = k
                    tobedeleted.append(k[0])
        elif "(" in z[2][0] and "(" in z[3][0]:
            for k in forest:
                if k[0] in z[2][0]:
                    z[2] = k
                    tobedeleted.append(k[0])
                elif k[0] in z[3][0]:
                    z[3] = k
                    tobedeleted.append(k[0])
    forestcopy = forest[:]
    for m in forestcopy:
        if m[0] in tobedeleted:
            forest.remove(m)
    return forest

def function_validator(txt):
    txt = txt.replace(" ", "")
    funcName, func = txt.split("=")
    if "+" in func:
        splitFunc= func.split("+")
        func = "+"
    elif "-" in func:
        splitFunc= func.split("-")
        func = "-"
    elif "^" in func:
        splitFunc= func.split("^")
        func = "^"
    elif "*" in func:
        splitFunc= func.split("*")
        func = "*"
    funcName = funcName.split("(")[0]
    return [funcName, func, splitFunc[0], splitFunc[1]]