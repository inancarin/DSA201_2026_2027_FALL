import math

def encode(s):
    s = s.replace(" ", "") # remove the spaces
    L = len(s)
    row = int(math.sqrt(L))
    col = row
    if row * col < L:
        col += 1
    
    main_list = []
    for i in range(row):
        temp = []
        for j in range(col):
            idx = i * col + j
            if idx < L:
                ch = s[idx]
            else:
                ch = ""
            temp.append(ch)
        main_list.append(temp)
    
    res = ""
    for j in range(col):
        for i in range(row):
            res += main_list[i][j]
        res += " "
    
    return res[:-1]


# main
s = "if man was meant to stay on the ground god would have given us roots"
res = encode(s)
print(res)