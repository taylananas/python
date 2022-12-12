import subprocess,sys

cases = open("kt.txt")
answers = open("ko.txt")

tempcases = cases.read().splitlines()
tempanswers = [*map(int, answers.read().splitlines())]
print(tempcases,tempanswers)
cases.close()
answers.close()

def testing(input,output):