import Factorial
import time, math

if __name__ == "__main__":
    
    start = time.time()
    for i in range(1000000):
        res = Factorial.factorial(100)
    end = time.time()
    elapsed_time = end - start
    print("Elapsed time for recursion is:", elapsed_time, "seconds.")

    start = time.time()
    for i in range(1000000):
        res2 = Factorial.factorial_wout_recursion(100)
    end = time.time()
    elapsed_time = end - start
    print("Elapsed time for iterative is:", elapsed_time, "seconds.")

    start = time.time()
    for i in range(1000000):
        res3 = math.factorial(100)
    end = time.time()
    elapsed_time = end - start
    print("Elapsed time for math module is:", elapsed_time, "seconds.")