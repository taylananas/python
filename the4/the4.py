class Tree():
    def create_tree():
        return []

    def name(T):
        return T[0]

    def left(T):
        return T[2]

    def right(T):
        return T[3]
    
    def is_empty(T):
        return T==[]

    def create_node(T,funcName, func,element1=[], element2=[]):
        T.extend([funcName, func, [element1], [element2]]) 


def construct_forest(defs):
    forest = []
    for funct in defs:
        branch = Tree.create_tree()
        functlist = function_validator(funct)
        checks = check_if_func(functlist)
        if checks == (0,0):
            Tree.create_node(branch,functlist[0],functlist[1],functlist[2],functlist[3])
        elif checks == (1,1):
            k = function_validator(funct)
            Tree.create_node(branch,k[0],k[1],k[2],k[3])
        elif checks[0] == 1:
            k = function_validator(funct)
            Tree.create_node(branch,k[0],k[1],k[2],k[3])
        elif checks[1] == 1:
            k = function_validator(funct)
            Tree.create_node(branch,k[0],k[1],k[2],k[3])
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

def check_if_func(txt):
    checklist = []
    for zort in txt[2:4]:
        if "(" in zort:
            checklist.append(1)
        else:
            checklist.append(0)

    if checklist[0] == 0 and checklist[1] == 0: return 0,0
    elif checklist[0] == 1 and checklist[1] == 0:   return 1,0
    elif checklist[0] == 0 and checklist[1] == 1:   return 0,1
    elif checklist[0] == 1 and checklist[1] == 1:   return 1,1

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
