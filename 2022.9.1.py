data = [x.rstrip() for x in open('data.txt', 'r')] 

hx = 0
hy = 0
tx = 0
ty = 0
visited = set()
visited.add((0,0))

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
        

for move in move_list:
    for i in range(move['s']):
        hx += move['x']
        hy += move['y']
        if (hx, hy) == (tx, ty):
            pass #head and tail same
        elif (abs(hx - tx) < 2 and abs(hy - ty) < 2):
            pass #tail adjacent to head
        elif (abs(hx - tx) == 2 and hy == ty):#tail is 2 above or below head
            tx =  (hx + tx)/ 2 
            visited.add((tx, ty))
        elif (abs(hy - ty) == 2 and  hx == tx):#tail is 2 left or right of head
            ty = (hy + ty)/ 2 
            visited.add((tx, ty))
        elif (abs(hx - tx) == 2 and abs(hy - ty) == 1):#tail is 2 above/below and 1 left/right of head
            ty = hy
            tx = (hx + tx)/ 2
            visited.add((tx, ty))
        elif (abs(hy - ty) == 2 and abs(hx - tx) == 1):#tail is 1 above/below and 2 left/right of head
            tx = hx
            ty = (hy + ty)/ 2
            visited.add((tx, ty))
print(len(visited))
