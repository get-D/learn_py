# Write a function multiply(a, b) that has a proper docstring explaining what
# it does. Then use help(multiply) to display the docstring.


def multiply(a,b):
    """
    To multipy two numbers
    
    :int a: first number 
    :int b: second number

    this function will return the multiplication of a and b
    """
    return a*b

def help(fun):
    print(f"Docstring of {fun}:", fun.__doc__)

help(multiply)