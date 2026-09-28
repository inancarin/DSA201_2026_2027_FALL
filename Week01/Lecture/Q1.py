def findMostFreq(arr):
    d = {} # d = dict()

    for elem in arr:
        if elem not in d:
            d[elem] = 1
        else:
            d[elem] += 1
    
    mostFreqItems = []
    maxValue = max(d.values())
    for k, v in d.items():
        if v == maxValue:
            mostFreqItems.append(k)
    
    return min(mostFreqItems)

# main part
arr = [4, 1, 2, 4, 1, 2, 3, 2, 4, 1]
res = findMostFreq(arr)
print(res)