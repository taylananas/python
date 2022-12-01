import subprocess, sys, threading,time

cases = open("cases.txt")
answers = open("answers.txt")

tempcases = cases.read().splitlines()
tempanswers = [*map(float, answers.read().splitlines())]
cases.close()
answers.close()

def testing(input,append_list,i):
    k = subprocess.check_output(f"{sys.executable} the2.py", input=input, encoding="utf")
    append_list[i]=float(k)

def grading():
    total = len(tempcases)
    grade = 0
    wrongs = []
    testanswers = [*range(total)]
    for i in range(total):
        thread = threading.Thread(target=testing,args=[tempcases[i],testanswers,i])
        thread.start()
    print(testanswers)
    for i in testanswers:
        pass
        # else: 
        #     diff = abs(i-float(testanswers[i]))
        #     wrongs.append(i,diff)
    print(f"Grade: {grade}")
    if wrongs:
        print(f"Wrongs: {wrongs}")


grading()