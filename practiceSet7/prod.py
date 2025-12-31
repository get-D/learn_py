# Use reduce() from functools to find the product of all elements in [1, 2, 3, 4]

from functools import reduce

l = [1, 2, 3, 4]

p = reduce(lambda x, y: x*y , l)

print(f"product of {l} is {p}")

