# Take a user input string and check if it is a palindrome

txt = input("Enter text: ")

if (txt == txt[ : : -1]):
    print("given string is a palindrome")
else:
    print("given string is not a palindrome")