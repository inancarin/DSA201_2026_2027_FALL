def factorial(n):
    if n < 0:
        return
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

def factorial_wout_recursion(n):
    if n < 0:
        return
    if n == 0:
        return 1
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

# main
if __name__ == "__main__":
    res = factorial_wout_recursion(5)
    print(res)