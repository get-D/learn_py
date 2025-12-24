# Convert the tuple to a list, change its first element to 50 , and convert it back to a tuple.

coordinates = (10, 20)

coList = list(coordinates)

coList[0] = 50

coordinates = tuple(coList)
print(f"changed tuple is {coordinates}")