import re
data = [x.rstrip() for x in open('data.txt', 'r')]

data = [re.findall('\d+', x) for x in data]

result = 0
for line in data:
    range1 = set(range(int(line[0]), int(line[1]) +1))
    range2 = set(range(int(line[2]), int(line[3]) +1))
    if range1.intersection(range2): result += 1

print (result)
