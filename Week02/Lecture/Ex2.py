if __name__ == "__main__":
    x = input("Enter a string: ")
    s = set()
    for ch in x:
        if ch.isalpha():
            """
            if ch not in s:
                s.add(ch)
            """
            s.add(ch)
    print(len(s))