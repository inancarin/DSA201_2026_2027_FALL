def isPangram(s):
    letters = {}
    for ch in s:
        if ch.isalpha():
            ch = ch.lower()
            if ch not in letters:
                letters[ch] = 1
            else:
                letters[ch] += 1
    
    if len(letters) == 26:
        return "pangram"
    else:
        return "not pangram"

# main part
s = "We promptly judged antique ivory buckles for the next prize"
s2 = "We promptly judged antique ivory buckles for the prize"
res = isPangram(s2)
print(res)
