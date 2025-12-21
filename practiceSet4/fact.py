# Write a recursive function factorial(n) that returns the factorial of a number.

def factorial(n):
    if (n == 0):
        return 1
    return n*factorial(n-1)

num = int(input("Enter a number: "))
fact = factorial(num)

print(f"Factorial of {num} is", fact)