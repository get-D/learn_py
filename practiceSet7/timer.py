#  Write a decorator  timer that calculates how long a function takes to execute.
# Test it with a function that sums numbers from 1 to 1,000,000.



from time import time


def timer(fun):
    def calc(n):
        t1 = time()
        result = fun(n) 
        t2 = time()
        print(t2-t1)
        return result
    return calc


@timer
def sum(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return f"sum is: {s}"
    

a = sum(1000000)
print(a)

