"""
There was a bug in the given solution

def is_beautiful(s):
    for i in range(len(s)):
        if s[i] == s[i+1]:
            return "not beautiful"
    return "beautiful"

    
- At first glance, this looks fine: it compares each character with the next one.
- It works well for "not beautiful" cases.
- However, when the string does not have two consecutive same characters ("beautiful" cases), then there is a problem.

The bug is
- The loop runs from i = 0 all the way to len(s)-1.
- When i = len(s)-1, the code tries to access s[i+1], which is out of range.

Below is the correct solution
"""

def is_beautiful(s):
    for i in range(len(s) - 1):   # FIX: loop until second-to-last char
        if s[i] == s[i+1]:
            return "not beautiful"
    return "beautiful"

res = is_beautiful("abcd")
print(res)