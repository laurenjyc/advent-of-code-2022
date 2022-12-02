total = 0
max = 0
with open("day-01-input.txt") as f:
    for i in f.readlines():
        if i.strip() == "":
            if total > max:
                max = total
            total = 0
        else:
            total += int(i)

print(max) # Ans: 73211