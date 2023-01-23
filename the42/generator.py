
import random

def generator():
    
    names = ["a","b","c","d","e","f","g","h","j","k","l","m","n"]
    operators = ["*","+","-","^"]

    constants = []
    for i in range (1,100):
        constants.append(str(i))

    all_funcs = []
    for i in names:
        func = i + "(x)" 
        all_funcs.append(func)

    terms = all_funcs + ["x"]

     
    case = []
    for i in range(6):
        func_to_be_used = random.choice(all_funcs)
        op_to_be_used = random.choice(operators)
        term_1 = random.choice(terms)
        term_2 = random.choice(constants)
        number_of_spaces = random.choice(range(1,6))*" "

        lil_case = func_to_be_used + "=" + number_of_spaces + term_1 + op_to_be_used + number_of_spaces+ term_2
        case.append(lil_case)

    str_case = str(case)
    outfile =open("cases.txt","a")
    outfile.writelines(str_case + "\n") 
    outfile.close 
 



