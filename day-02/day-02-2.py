arr = ['A', 'B', 'C']
score = 0
with open("day-02-input.txt") as f:
    for i in f.readlines():
        opp, result = i.split()
        if result == "X":
            score += arr.index(arr[(arr.index(opp) - 1) % 3]) + 1
        elif result == "Y":
            score += 3 + arr.index(opp) + 1
        else:
            score += 6 + arr.index(arr[(arr.index(opp) + 1) % 3]) + 1

print(score) # Ans: 14859