# Combine a decorator with *args and **kwargs support so it can wrap any function regardless of its parameters.


def dec(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        func(*args, **kwargs)
        print("After function call")
    return wrapper

@dec
def greet(name, age=None):
    print(f"Hello {name}, age={age}")

@dec
def add(a, b):
    return a + b

greet("Alice", age=20)
print(add(3, 5))
