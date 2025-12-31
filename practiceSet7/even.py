# Use filter() to get only even numbers from [10, 11, 12, 13, 14] .

l = [10,11,12,13,14]

even = list(filter(lambda x: x%2 == 0, l))

print(f"even numbers from {l} are {even}")

