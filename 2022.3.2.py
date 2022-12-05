data = [x.rstrip() for x in open('data.txt', 'r')]

score = 0
team = []
while len(data):
    team.append(set(data.pop(0)))
    team.append(set(data.pop(0)))
    team.append(set(data.pop(0)))
   
    badge = (team[0].intersection(team[1])).intersection(team[2]).pop()
    if badge.isupper():
        score +=  1 + 26 + ord(badge) - ord('A')
    else:
        score += 1 + ord(badge) - ord('a')
    team = []
    
print (score)  
