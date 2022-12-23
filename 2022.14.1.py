source = 'data.14.txt'
data = [x.rstrip() for x in open(source, 'r')]
data = [x.split(' -> ') for x in data]
data = [[[int(x) for x in item] for item in [x.split(',') for x in datarow]] for datarow in data]
rocks = set()
sand = set()


def add_rocks(first, second):
    x1 = first[0]
    y1 = first[1]
    x2 = second[0]
    y2 = second[1]
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
        
                

def move_sand(from_, lowest_rock, grid):
    (x, y) = from_
    
    if ((x , y + 1)) not in grid:
        if (y + 1) == lowest_rock:
            return 0
        from_ = move_sand((x, y + 1), lowest_rock, grid)
    elif ((x - 1, y + 1)) not in grid:
        
        if (y + 1) == lowest_rock:
            return 0
        from_ = move_sand((x - 1, y + 1), lowest_rock, grid)
    elif ((x + 1, y + 1)) not in grid:
        
        if (y + 1) == lowest_rock:
            return 0
        from_ = move_sand((x + 1, y + 1), lowest_rock, grid)
    
    return(from_)


def add_sand(rocks, sand, lowest_rock):
    while 1:
        occupied = rocks.union(sand)
        new_sand = move_sand((500, 0), lowest_rock, occupied)
        if new_sand == 0 : break
        else:
            sand.add(new_sand)
    print(len(sand))
    
#populate rocks
for lines in data:
    for i in range(len(lines)-1):
        rocks = rocks.union(add_rocks(lines[i], lines[i + 1]))
        
lowest_rock =max([rock[1] for rock in rocks])
add_sand(rocks, sand, lowest_rock)
