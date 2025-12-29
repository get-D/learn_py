# Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function say_hello() that prints "Hello!" .

def logger(fun):
    def intro():
        print("Function is being called")
        fun()
    return intro

@logger
def say_hello():
    print("Hello!")

say_hello()
