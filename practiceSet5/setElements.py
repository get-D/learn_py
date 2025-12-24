# Add 5 to the set, remove 2 , and check if 4 is in the set

my_set = {1, 2, 3, 3, 4}

my_set.add(5)
my_set.remove(2)

if 4 in my_set:
    print("set has element 4")
else:
    print("set does not have element 4")

print("Set:", my_set)