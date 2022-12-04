data = [x.rstrip() for x in open('data.txt', 'r')]

def process_round(round):
    round = round.split()

    # convert A, B, C  into ints 0, 1, 2
    they = ord(round[0]) - ord('A')
    outcome = round[1]
    
    if outcome == 'X':
        me = (they - 1)%3
        return (me + 1)
    if outcome == 'Y':
        return (they + 1 + 3)
    if outcome == 'Z':
        me = (they + 1)%3
        return (me + 1 + 6)

   

score = 0
for x in data:
    score += process_round(x)
print (score)
