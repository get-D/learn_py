# Write a function safe_divide(a, b) that returns the result of a / b , but
# returns "Cannot divide by zero" if b is 0

def safe_divide(a, b):
    if b == 0 :
        return "Cannot divide by zero"
    return a / b

d1 = safe_divide(34,5)
d2 = safe_divide(34,0)
d3 = safe_divide(36,9)

print(d1)
print(d2)
print(d3)