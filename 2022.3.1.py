data = [x.rstrip() for x in open('data.txt', 'r')]

score = 0
for x in data:
    midpoint = int(len(x)/2)
  
    first_half = set(x[:midpoint])
    second_half = set(x[midpoint:])
    misplaced = first_half.intersection(second_half).pop()
    if misplaced.isupper():
        score +=  1 + 26 + ord(misplaced) - ord('A')
    else:
        score += 1 + ord(misplaced) - ord('a')
    
print (score) 
