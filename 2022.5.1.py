data = [x.rstrip() for x in open('data.txt', 'r')]
import re

#starting crates position data ends here
end_start = ' 1   2   3   4   5   6   7   8   9'

#set up the initial crates state
initial = []
for line in data:
    if line == end_start: break
    initial.append(line)
#parse the move lines
moves = [x for x in data if 'move' in x]

#parse the stacks into a dict
stacks = {}
for i in range(1, 10): stacks[i]=[]

for line in initial:
    for x in range(len(line)):
        if line[x].isupper():
            stacks[1 + int(x/4)].append(line[x])

#parse the moves data- how many, from, to
moves = [re.findall('\d+', x) for x in moves]

for line in moves:
    how_many = int(line[0])
    from_stack = int(line[1])
    to_stack = int(line[2])
    #move the crates, one at a time
    for i in range(how_many):
        stacks[to_stack].insert(0, stacks[from_stack].pop(0))

answer = ''
for key in stacks:
    answer += stacks[key][0]
    

print (answer)
