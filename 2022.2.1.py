data = [x.rstrip() for x in open('data.txt', 'r')]

def process_round(round):
    round = round.split()

    # convert A, B, C X, Y, Z into ints 0, 1, 2
    they = ord(round[0]) - ord('A')
    me = ord(round[1]) - ord('X')
    
    #tie earns 3 pts
    if me == they: win_points = 3
    #lose, my choice is adjacent ccw to theirs
    elif (they - me)%3 == 1: win_points = 0
    #win, my choice is adjacent cw to theirs
    elif (they - me)%3 == 2: win_points = 6
    
    # add the points from the object you chose (= me + 1)
    return (win_points + me + 1)
   

score = 0
for x in data:
    score += process_round(x)
print (score)
