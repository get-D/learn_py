# Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.

def fib(n):
    if( n == 0 or n == 1):
        return n
    return fib(n-1) + fib(n-2)

def fibonacci(n):
    for i in range(n):
        print(fib(i))
    

num = int(input("Enter a number: "))

print(f"first {num} Fibonacci numbers:")
fibonacci(num)

