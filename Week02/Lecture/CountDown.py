def countdown_wout_rec(n):
    for i in range(n, -1, -1): #n, n-1, n-2, ..., 3, 2, 1, 0
        print(i)

def countdown(n):
    print(n)
    if n > 0:
        countdown(n-1)

#countdown_wout_rec(10)
countdown(10)