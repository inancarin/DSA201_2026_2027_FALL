"""
The solution given by chatGPT works correctly, however it is very inefficient when we have huge number of numbers.
The reason for the inefficiency is that it repeatedly makes searches on the list.
Instead we can make these searches with a dictionary to make it more efficient.

"""

def first_repeated_chatGPT(arr):
    seen = []
    for num in arr:
        if num in seen:  
            return num
        seen.append(num)
    return -1

def first_repeated_dict(arr):
    seen = {}
    for num in arr:
        if num in seen:
            return num
        seen[num] = True # here True value is not important, instead it could be 1 or something else
    return -1


# let's simulate this
myNumbers = list(range(1, 100001)) # contains all numbers from 1 to 100001
myNumbers.append(4) # add a duplicated element

# compare following two lines
res = first_repeated_dict(myNumbers)
#res = first_repeated_chatGPT(myNumbers)
print(res)