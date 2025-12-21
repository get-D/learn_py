# Create a small module my_utils.py with a function is_even(n) that returns
# True if n is even. Import and use it in another Python file.


import myutils

num = int(input("Enter a number: "))

if(myutils.is_even(num) == True):
    print("Number is even")
else:
    print("Number is odd")