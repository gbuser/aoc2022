data = [x.rstrip() for x in open('data.txt', 'r')]

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == 'S':
            start = (y, x)
        if data[y][x] == 'E':
            end = (y, x)

data = [[(ord(x) - ord('a')) for x in y]  for y in data]
data[start[0]][start[1]] = 0
data[end[0]][end[1]] = ord('z') - ord('a')

class node():
    def __init__(self, y, x, data,  parent = None):
        self.y = y
        self.x = x
        self.h = 0
        self.g = 0
        self.f = 0
        self.parent = parent
        self.height = data[y][x]
        
    def set_h(self, end):
        self.h = abs(self.x - end.x) + abs(self.y - end.y)
        
    def get_neighbors(self, nodes):
        
        offsets = {(1,0), (-1, 0), (0, 1), (0, -1)}
        neighbors = []
        if self.y == 0:
            offsets.remove((-1, 0))
        if self.y == len(nodes) - 1:
            offsets.remove((1, 0))
        if self.x == 0:
            offsets.remove((0, -1))
        if self.x == len(nodes[0]) - 1:
            offsets.remove((0, 1))
        for item in offsets:
            possible_neighbor = nodes[self.y + item[0]][self.x + item[1]]
            if self.height + 1 >= possible_neighbor.height:
                neighbors.append(possible_neighbor)
        return neighbors
    
            
def get_lowest(nodes):
    low = 1000
    for node in nodes:
        if node.f < low:
            low = node.f
            lowest_node = node
    return lowest_node
        
nodes = [[] for y in range(len(data))]
for y in range(len(data)):
    for x in range(len(data[0])):
        nodes[y].append(node(y, x, data))   
        
start = nodes[start[0]][start[1]]
end = nodes[end[0]][end[1]]

for y in range(len(data)):
    for x in range(len(data[0])):
        nodes[y][x].set_h(end)
        

open_nodes = set()
closed_nodes = set()
open_nodes.add(start)


current_node = get_lowest(open_nodes)
while current_node != end:
    closed_nodes.add(current_node)
    open_nodes.remove(current_node)
    neighbors = current_node.get_neighbors(nodes)
    
    
    for neighbor in neighbors:
        if neighbor in closed_nodes: 
            continue
        if neighbor not in open_nodes:
            neighbor.parent = current_node
            neighbor.g = current_node.g + 1
            neighbor.f = neighbor.g + neighbor.h
            open_nodes.add(neighbor)
        elif neighbor in open_nodes:
            if neighbor.g > (current_node.g + 1):
                neighbor.g = current_node.g + 1
                neighbor.parent = current_node
                neighbor.f = neighbor.g + neighbor.h
               
    current_node = get_lowest(open_nodes)
print(current_node.g)
