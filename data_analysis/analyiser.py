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
name_count = collections.Counter(names)
c = []