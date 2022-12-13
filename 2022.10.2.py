data = [x.rstrip() for x in open('data.txt', 'r')]
data = [x.split()[-1] for x in data]
data = [(int(x) if x!= 'noop' else x) for x in data]

sprite = 1
cycle = 0
display = str()

def cycle_this(cycle, sprite):
    #current crt position = (cycle -1)%40. if sprite is <=1 away from crt, it gets lit
    if abs((cycle-1)%40 - sprite) <=1: 
        return '#'
    else:
        return ' '
    
for line in data:
    cycle += 1
    display += (cycle_this(cycle, sprite))
    
    if (line != 'noop'):
        cycle += 1
        display += (cycle_this(cycle, sprite))
        sprite += line
    
for i in range(6):
    print(display[i*40: (i*40 + 40)])
