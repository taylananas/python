from the4 import construct_forest

cases = open("cases").read().splitlines()
answers = open("answers").read().splitlines()

for i,value in enumerate(cases):
    value = eval(value)
    temp = []
    answer = construct_forest(value)
    print(answer)

    if answer != eval(answers[i]):
        print("wrong")
    else:
        print("true")