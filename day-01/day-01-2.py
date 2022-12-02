total = 0
max_arr = [0,0,0]
with open("day-01-input.txt") as f:
    for i in f.readlines():
        if i.strip() == "":
            for j in range(len(max_arr)):
                if total > max_arr[j]:
                    max_arr[j] = total
                    break 
            total = 0
        else:
            total += int(i)

print(sum(max_arr)) # Ans: 213958