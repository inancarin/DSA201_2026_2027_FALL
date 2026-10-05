def countRecursively(names):
    cnt = 0
    for elem in names:
        if isinstance(elem, list):
            cnt += countRecursively(elem)
        else:
            cnt += 1
    return cnt

if __name__ == "__main__":
    names = ["Adam", ["Bob", ["Chet","Cat"], "Barb", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
    res = countRecursively(names)
    print("Result is", res)