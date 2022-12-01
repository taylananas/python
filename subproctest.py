cases = open("kt.txt")
answers = open("ko.txt")

tempcases = cases.read().splitlines()
tempanswers = answers.read().splitlines()

cases.close()
answers.close()

def testing(input,output):