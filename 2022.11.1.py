data = [x.rstrip() for x in open('data.txt', 'r')]
import re

class monkey():
    def __init__(self, details):
        self.items = [int(x) for x in re.findall('\d+', details[0])]
        self.op = re.search('old.*', details[1]).group()
        self.test = int(re.search('\d+', details[2]).group())
        self.true = int(re.search('\d', details[3]).group())
        self.false = int(re.search('\d', details[4]).group())
        self.inspected = 0
        
    def turn(self, monkeys):
        for item in self.items:
            old = item
            new = int(eval(self.op)/ 3)
            if new % self.test == 0:
                monkeys[self.true].items.append(new)
            else:
                monkeys[self.false].items.append(new)
            self.inspected += 1
            self.items = []
                
monkeys = []
while len(data):#populate the monkey list
    monkeys.append(monkey(data[1:6]))
    data = data[7:]
    
for i in range(20):
    for monkey in monkeys:
        monkey.turn(monkeys)
    i += 1

activity = [x.inspected for x in monkeys]
activity.sort()
print(activity[-1] * activity[-2])
