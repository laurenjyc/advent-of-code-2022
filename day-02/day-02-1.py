dict = {'A': 'X', 'B': 'Y', 'C': 'Z'}
dict2 = {'A': 'Y', 'B': 'Z', 'C': 'X'}
dict3 = {'X': 1, 'Y': 2, 'Z': 3}
score = 0

with open("day-02-input.txt") as f:
    for i in f.readlines():
        opp, me = i.split()
        
        score += dict3[me]
        if dict2[opp] == me:
            score += 6
        elif dict[opp] == me:
            score += 3
    
print(score) # Ans: 10310