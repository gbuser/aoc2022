data = [x.rstrip() for x in open('data.txt', 'r')]
temp = []

for line in data:
    temp.append([int(x) for x in line])
data = temp   

def is_vis(y_pos, x_pos, data, cols):
    height = data[y_pos][x_pos]
    north = cols[x_pos][:y_pos]
    south = cols[x_pos][y_pos + 1:]
    east = data[y_pos][x_pos + 1:]
    west = data[y_pos][:x_pos]
    directions = [north, south, east, west]
    for dir in directions:
        if height > max(dir):
            return True
    return False

cols = [[] for x in range (len(data[0]))]
rows = data

for x in range(len(rows)):
    for row in rows:
        cols[x].append(row[x])

score = 0
for y in range(1, len(data) -1):
    for x in range(1, len(data[0]) - 1):
        if is_vis(y, x, data, cols):
            score += 1

print(score + (len(data) - 1) *4)
