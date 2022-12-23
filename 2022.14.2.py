source = 'data.14.txt'
data = [x.rstrip() for x in open(source, 'r')]
data = [x.split(' -> ') for x in data]
data = [[[int(x) for x in item] for item in [x.split(',') for x in datarow]] for datarow in data]
rocks = set()
sand = set()


def add_rocks(first, second):
    (x1, y1) = first
    (x2, y2) = second
    new_rocks = set()
    if x1 == x2:
        if y2 > y1:
            for i in range(y1, y2 + 1):
                new_rocks.add((x1, i))
        if y2 < y1:
            for i in range(y2, y1 + 1):
                new_rocks.add((x1, i))
    elif y1 == y2:
        if x2 > x1:
            for i in range(x1, x2 + 1):
                new_rocks.add((i, y1))
        if x2 < x1:
            for i in range(x2, x1 + 1):
                new_rocks.add((i, y1))
    return new_rocks
 
def move_sand(from_, bottom, occupied):
    (x, y) = from_
    if y + 1 == bottom:
        return from_
    if (x, y + 1) not in occupied:
        return move_sand2((x, y + 1), bottom, occupied)
    if (x -1, y + 1) not in occupied:
        return move_sand2((x - 1, y + 1), bottom, occupied)
    if (x + 1, y +1) not in occupied:
        return move_sand2((x + 1, y + 1), bottom, occupied)
    return from_
    
def add_sand(rocks, sand, bottom):
    while 1:
        occupied = rocks.union(sand)
        new_sand = move_sand2((500, 0), bottom, occupied)
        sand.add(new_sand)
        if new_sand == ((500, 0)): break
    print(len(sand))
    
#populate rocks
for lines in data:
    for i in range(len(lines)-1):
        rocks = rocks.union(add_rocks(lines[i], lines[i + 1]))
        
lowest_rock =max([rock[1] for rock in rocks])
bottom = lowest_rock + 2
add_sand(rocks, sand, bottom)
