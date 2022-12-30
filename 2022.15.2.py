import re
data = [x.rstrip() for x in open('data.15.txt', 'r')]
data = [re.findall('-?\d+', x) for x in data]
data = [[int(x) for x in y] for y in data]
start_limit = 0
finish_limit = 4000000

def manhattan_distance(points):
    x1 = points[0]
    y1 = points[1]
    x2 = points[2]
    y2 = points[3]
    return (abs(x1 - x2) + abs(y1 - y2))


#returns points, if any in a given row excluded by one sensor
def exclude_from_row(row, sensor, start_limit, finish_limit):
    half_span = sensor['md'] - abs(row - sensor['y'])
    if half_span >= 0:
        start = sensor['x'] - half_span
        if start < start_limit:
            start = start_limit
        finish = sensor['x'] + half_span
        if finish > finish_limit:
            finish = finish_limit
        return(start, finish)
    else: 
        return None

#generates a list of ranges excluded at one row by all the sensors and sends to compact()
def eval_row(row, sensors, finish_limit):
    excludes = []
    for sensor in sensors:
        excludes.append(exclude_from_row(row, sensor, 0, finish_limit))
    excludes = [x for x in excludes if x]
    excludes.sort()
    if compact(excludes):
        print(f"Row {row} fails at {compact(excludes)-1}")
        print(f"answer is {4000000 *(compact(excludes)-1) + row}")
      
#takes a list of excluded ranges and returns any which are not continuous, the hole must be here
def compact(spans):
    start = 0
    finish = spans[0][1]
    for span in spans[1:]:
        if span[0] > finish + 1:
            return span[0]
        if span[1] > finish:
            finish = span[1]
    return False


sensors = []
for line in data:
    sensors.append({'x': line[0], 'y': line[1], 'md': manhattan_distance(line)})

for i in range(4000001):
    eval_row(i, sensors, finish_limit)
