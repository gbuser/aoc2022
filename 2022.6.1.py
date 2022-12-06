data =[x.rstrip() for x in open('data.txt', 'r')][0]

these_four = data[:4]
char_count = 4
while 1:
    these_four = these_four[1:]
    these_four += (data[char_count])
    char_count += 1
    if len(set(these_four)) == 4: break
print(char_count)
