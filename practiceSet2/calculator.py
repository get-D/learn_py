# Write a program using match case that simulates a simple calculator.
# Ask the user for two numbers and an operation (+, -, *, /).
# Perform the operation using match case .


x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
op = input("Select operation (+, -,*, / ): ")

match op :
    case "+" :
        print("Sum is", x+y)
    case "-" :
        print("Difference is", x-y)
    case "*" :
        print("Product is", x*y)
    case "/" :
        print("Quotient is", x/y)
    case _ :
        print("invalid operation input")