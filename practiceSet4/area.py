# Write a function calculate_area(length, width=10) that returns the area of
# a rectangle. Test it by calling the function with:
# Both length and width
# Only length (use default width)

def calculate_area(length, width=10):
    return length*width

a1 = calculate_area(43, 23)
a2 = calculate_area(43)

print("without defalt width:", a1)
print("with defalt width:", a2)