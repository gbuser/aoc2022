data = [x.rstrip() for x in open('data.txt', 'r')] 

class knot:
    def __init__(self):
        self.x = 0
        self.y = 0
    #move the next knot depending on where the prior knot is. note the final elif is necessary
    #because if the knot began diagonally adjacent, it's possible for the more proximal knot to move
    #one more diagonal step away, not possible when there was just head and tail knots
    def move(self, prior):
        if (abs(prior.x - self.x) < 2 and (abs(prior.y - self.y) < 2)):
            return #knots are adjacent or superimposed
        elif (abs(prior.x - self.x) == 2 and (prior.y == self.y)):
            self.x = int((prior.x + self.x)/2) #knots are 2 apart horizontally
        elif (abs(prior.y - self.y) == 2 and (prior.x == self.x)):
            self.y = int((prior.y + self.y)/2) #knots are 2 apart verticaly
        elif (abs(prior.x - self.x) == 2 and abs(prior.y - self.y) == 1):
            self.x = int((prior.x + self.x) / 2 ) 
            self.y = prior.y #knots apart 2 horizontally, 1 vertically
        elif (abs(prior.y - self.y) == 2 and abs(prior.x - self.x) == 1):
            self.y = int((prior.y + self.y)/ 2)
            self.x = prior.x #knots apart 1 horizontally, 2 vertically
        elif (abs(prior.y - self.y) == 2 and abs(prior.x - self.x) == 2):
            self.y = int((prior.y + self.y)/ 2)
            self.x = int((prior.x + self.x)/ 2) # knots apart 2 diagonally
            
move_list = []
for line in data:
    this_move = {'x' :0, 'y' : 0, 's':0}
    line = line.split()
    if line[0] == 'R':
        this_move['x'] = 1
    if line[0] == 'L':
        this_move['x'] = -1
    if line[0] == 'U':
        this_move['y'] = 1
    if line[0] =='D':
        this_move['y'] = -1
    this_move['s'] = int(line[1])
    move_list.append(this_move)
 

knots = [knot() for i in range(10)]
head = knots[0]
tail = knots[-1]
visited = set()
visited.add((0,0))

for move in move_list:
    for i in range(move['s']):
        head.x += move['x']
        head.y += move['y']
        
        for j in range(1, len(knots)):
            (pre_x, pre_y) = (knots[j].x, knots[j].y)
            knots[j].move(knots[j - 1])
            if (knots[j].x, knots[j].y) == (pre_x, pre_y): break
            
        visited.add((tail.x, tail.y))
print(len(visited))
