

if __name__ == "__main__":
    x = input("Enter a string: ")
    d = {} # d = dict() 
    for ch in x:
        if ch.isalpha():
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
    
    maxValue = max(d.values())
    for k,v in d.items():
        if v == maxValue:
            print(k, maxValue)