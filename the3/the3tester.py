from the3 import pattern_search
grade = 0
wrongs = []
f = open("test_images")
images = f.read().splitlines()
f.close()
f = open("test_patterns")
patterns = f.read().splitlines()
f.close()
f = open("answers")
answers = f.read().splitlines()
f.close()
l = 0
tested_answers = []
for image in images:
    image = eval(image)
    for i in patterns[l*20 : (l + 1)*20]:
        i = eval(i)
        a = pattern_search(i,image)
        tested_answers.append(a)
    l += 1
for i in range(len(answers)):
    if str(answers[i]) == str(tested_answers[i]):
        grade += 1
    else:
        wrongs.append([i, i//20, answers[i], tested_answers[i]])
print(f"Grade: {grade}")
if wrongs:
    print("INDEX, IMAGE INDEX, TRUE ANSWER, YOUR ANSWER")
    for i in wrongs:
        print(i)