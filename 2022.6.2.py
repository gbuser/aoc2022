data =[x.rstrip() for x in open('data.txt', 'r')][0]

these_fourteen = data[:14]
char_count = 14
while 1:
    these_fourteen = these_fourteen[1:]
    these_fourteen += (data[char_count])
    char_count += 1
    if len(set(these_fourteen)) == 14: break
print(char_count, these_fourteen)
