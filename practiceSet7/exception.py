# Write a program that asks the user to enter a number and handles:
# ValueError if the input is not a number
# ZeroDivisionError if you try to divide by zero

# Create a custom exception NegativeNumberError and raise it when the user enters a negative number.


class NegativeNumberError(Exception):
    pass


try:
    x = int(input("Enter a number: "))

    if (x<0):
        raise NegativeNumberError("Number cannot be negative")
    
    y = 9/x
    print(f"result is {y}")

except ValueError:
    print("input is not a number.")

except ZeroDivisionError:
    print("cannot divide by zero.")

except NegativeNumberError as e:
    print(e)


