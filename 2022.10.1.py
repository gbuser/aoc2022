data = [x.rstrip() for x in open('data.txt', 'r')]
data = [x.split()[-1] for x in data]
data = [(int(x) if x!= 'noop' else x) for x in data]

x = 1
cycle = 0
answer = 0

for line in data:
    if line == 'noop':
        cycle += 1
        if (cycle <221 and (cycle-20)%40 == 0 ):
            answer += (x*cycle)
       
    else:
        cycle += 1
        if (cycle <221 and (cycle-20)%40 == 0 ):
            answer += (x*cycle)
        cycle += 1
        if (cycle <221 and (cycle-20)%40 == 0 ):
            answer += (x*cycle)
          
        x += line
    
print(answer)
