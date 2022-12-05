with open("day-03-input.txt") as f:
    total = 0
    i = f.readlines()
    for j in range(0,len(i),3):
        a = min(set(i[j].strip()), set(i[j+1].strip()), set(i[j+2].strip()), key=len)
        for char in a:
            if char in i[j] and char in i[j+1] and char in i[j+2]:
                cur = ord(char) - 96
                if cur < 0:
                    cur += 32 + 26
                total += cur

    print(total) # Ans: 2567