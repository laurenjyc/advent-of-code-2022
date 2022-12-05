import re
total = 0
with open("day-04-input.txt") as f:
    for i in f:
        a,b,c,d = re.split("[,-]", i.strip())
        a,b,c,d = int(a), int(b), int(c), int(d)
        if (b >= c and b <= d) or (d >= a and d <= b):
            total += 1

print(total) # Ans: 924