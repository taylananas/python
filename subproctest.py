import subprocess,sys

cases = open("kt.txt")
answers = open("ko.txt")

tempcases = cases.read().splitlines()
tempanswers = [*map(int, answers.read().splitlines())]
print(tempcases,tempanswers)
cases.close()
answers.close()

def testing():
    grade = 0
    total = len(tempcases)
    for i in range(total):
        k = subprocess.check_output(f"{sys.executable} subtest.py", input=tempcases[i], encoding="utf")
        k = float(k)
        if k == tempanswers[i]:
            print("correct")
            grade += 1
        else: print("wrong")
    print(f"{grade}/{total}")
testing()