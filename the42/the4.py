def construct_forest(functions):
    operators = ["+","-","*","^"]
    tempforest = []
    forest = []
    for i in functions:
        i = i.replace(" ","")
        tempforest.append(i)
    for i in tempforest:
        name = i[0]
        second = i.split("=")
        for operator in operators:
            if operator in second[1]:
                splitted = operator,second[1].split(operator)
        forest.append([name,splitted[0],[splitted[1][0]],[splitted[1][1]]])
    kopya = forest[:] #asil forestten silince for dongusu patliyor
    for function in kopya:
        for element in function:
            if ")" in element[0]:
                for func2 in kopya:
                    if element[0][0] == func2[0]:
                        function[function.index(element)] = func2
                        forest.remove(func2)
    return forest