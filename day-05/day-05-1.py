import re
with open("day-05-input.txt") as f:
    i = f.readlines()
    arr = []
    done = False
    for j in i:
        if not done:
            temp = j[1:len(j):4]
            if temp.isdigit():
                continue
            if not temp.strip():
                done = True
                continue
            
            for k in range(len(temp)):
                if len(arr) != len(temp):
                    if temp[k].strip():
                        arr.append([temp[k]])
                    else:
                        arr.append([])
                else:
                    if temp[k].strip():
                        arr[k].append(temp[k])
        else:
            num = re.findall("\d+", j)
            for total in range(int(num[0])):
                arr[int(num[2])-1].insert(0, arr[int(num[1])-1].pop(0))

    str = ""
    for t in arr:
        str += t[0] 
    print(str) # Ans: QNHWJVJZW