def countRecursively(names, d):
    for elem in names:
        if isinstance(elem, list):
            countRecursively(elem, d)
        else:
            if elem not in d:
                d[elem] = 1
            else:
                d[elem] += 1

if __name__ == "__main__":
    d = {}
    names = ["Adam", ["Bob", ["Alex","Bob"], "Barb", "Bert"], "Alex", ["Bea", "Alex"], "Ann"]
    countRecursively(names, d)
    print(d)