data = [x.rstrip() for x in open('data.txt', 'r')]

this_cal = 0
cal_list = []
for x in data:
    if len(x):
        this_cal += int(x)
    else:
        cal_list.append(this_cal)
        this_cal = 0

cal_list.sort()
print (sum(cal_list[-3:]))
