import math
with open("day-03-input.txt") as f:
    total = 0
    for i in f:
        i = i.strip()
        mid = math.floor(len(i)/2)
        a = min(set(i[:mid]), set(i[mid:]))

        if a == set(i[:mid]):
            b = set(i[mid:])
        else:
            b = set(i[:mid])

        for j in a:
            if j in b:
                cur = ord(j) - 96
                if cur < 0:
                    cur += 32 + 26
                total += cur

    print(total) # Ans: 8072