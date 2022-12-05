import re
total = 0
with open("day-04-input.txt") as f:
    for i in f:
        a,b,c,d = re.split("[,-]", i.strip())
        a,b,c,d = int(a), int(b), int(c), int(d)
        if (a <= c and b >= d) or (c <= a and d >= b):
            total += 1

print(total) # Ans: 562