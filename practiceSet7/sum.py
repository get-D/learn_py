# Write a function sum_all(*args) that accepts any number of integers and returns their sum


def sum_all(*args):
    sum = 0
    for i in args:
        sum += i

    return sum


print(sum_all(34,634,64,23,9))