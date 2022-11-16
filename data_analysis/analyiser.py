import csv
import collections

csv_file = open("MOCK_DATA.csv")
countries = []
names = []
m = f = 0
csv_reader = csv.reader(csv_file, delimiter=",")
for i in csv_reader:
    if i[4] == "Male":
        m +=1
    else:
        f +=1
    countries.append(i[5])
    names.append(i[1])

countries.sort()
a = collections.Counter(countries)
b =[]

for i in range(len(a.keys())):
    b.append([list(a.keys())[i],list(a.values())[i]])
c = 0
all_names = ""
temp2 = []
for i in names[1:]:
    temp2.append(i[0])
temp2.sort()
for i in temp2:
    all_names += i
print(all_names)
