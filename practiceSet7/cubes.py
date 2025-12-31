# Use map() to convert [1, 2, 3, 4, 5] into their cubes

ls = [1,2,3,4,5]

cubes = list(map(lambda x: pow(x, 3), ls))

print(f"cubes of {ls} are {cubes}")

