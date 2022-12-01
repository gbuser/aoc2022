data = [x.rstrip() for x in open('data.txt', 'r')]

max_cal = 0
this_cal = 0
for x in data:
    if len(x):
        this_cal += int(x)
    else:
        if this_cal > max_cal: max_cal = this_cal
        this_cal = 0
print (max_cal)
