data = [x.rstrip() for x in open('data.txt', 'r')]
temp = []

for line in data:
    temp.append([int(x) for x in line])
data = temp   
cols = [[] for x in range (len(data[0]))]
rows = data

for x in range(len(rows)):
    for row in rows:
        cols[x].append(row[x])
        
def how_many_trees(y_pos, x_pos, data, cols):
    height = data[y_pos][x_pos]
    north = cols[x_pos][y_pos - 1:: -1]
    south = cols[x_pos][y_pos + 1:]
    east = data[y_pos][x_pos + 1:]
    west = data[y_pos][x_pos -1:: -1]
    score = 1
    directions = [north, south, east, west]
    for direction in directions:
        this_dir =0
        for tree in direction:
            this_dir += 1
            if tree >= height: break
        score *= this_dir
    return score



best_score = 0
for y in range (1, len(data) - 1):
    for x in range (1, len(data[0]) - 1):
        this_tree_score = how_many_trees(y, x, data, cols)
        if this_tree_score > best_score:
            best_score = this_tree_score
print (best_score)
