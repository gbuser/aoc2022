data = [x.rstrip() for x in open('data.txt', 'r')]

#all this just to handle the S and E points
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == 'S':
            start = (y, x)
        if data[y][x] == 'E':
            end = (y, x)

#convert letters into ints
data = [[(ord(x) - ord('a')) for x in y]  for y in data]
data[start[0]][start[1]] = 0 #replace 'S' with 0
data[end[0]][end[1]] = ord('z') - ord('a') #replace 'E' with z height

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
        #manhattan distance from a node to the end
        self.h = abs(self.x - end.x) + abs(self.y - end.y)
        
    def get_neighbors(self, nodes):
        #returns a list of all valid neighbors, accounting for borders and height difference
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
    
            
def get_lowest(nodes):#returns node with lowest f value
    if len(nodes) == 0:
        return False
    else:
        lowest_node = nodes[0]
        for node in nodes:
            if node.f < lowest_node.f:
                lowest_node = node
        return lowest_node
    
def reset_grid(nodes, end):#resets the node to original state, cuz path algorithm changes them
    for y in range(len(nodes)):
        for x in range(len(nodes[0])):
            nodes[y][x].g = 0
            nodes[y][x].f = 0
            nodes[y][x].set_h(end)
        
nodes = [[] for y in range(len(data))]#populates nodes array
for y in range(len(data)):
    for x in range(len(data[0])):
        nodes[y].append(node(y, x, data))   
        
start = nodes[start[0]][start[1]]
end = nodes[end[0]][end[1]]

a_list = [] #create a list of nodes of a's for starting point
for y in range(len(data)):
    for x in range(len(data[0])):
        nodes[y][x].set_h(end)
        if nodes[y][x].height == 0:
            a_list.append(nodes[y][x])
        
def get_path_length(start, end, nodes): #A* algorithm with start, end and array
    current_node = start # start at the beginning
    open_nodes = {start}
    closed_nodes = set()
    while current_node != end: # and keep going to the end
        closed_nodes.add(current_node) #you're done with the current node, move from open to closed list
        open_nodes.remove(current_node)
        neighbors = current_node.get_neighbors(nodes)
        
        for neighbor in neighbors:
            if neighbor in closed_nodes: #do nothing, next neighbor
                continue
            if neighbor not in open_nodes: #not seen yet- assign parent, g and calculate f. add to open
                neighbor.parent = current_node
                neighbor.g = current_node.g + 1
                neighbor.f = neighbor.g + neighbor.h
                open_nodes.add(neighbor)
            elif neighbor in open_nodes: #update g if current is lower and change parent to current
                if neighbor.g > (current_node.g + 1):
                    neighbor.g = current_node.g + 1
                    neighbor.parent = current_node
                    neighbor.f = neighbor.g + neighbor.h
        
        current_node = get_lowest(list(open_nodes)) #make the node with lowest f current
        if current_node == False: #out of open_nodes and haven't reached end. no path
            return 0
    
    return current_node.g

path_lengths = []

for a in a_list:
    reset_grid(nodes, end)
    path_lengths.append(get_path_length(a, end, nodes)) 

paths = [x for x in path_lengths if x >0]

min(paths)
