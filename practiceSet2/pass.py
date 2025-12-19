# Write a program that keeps asking the user to enter a password until they enter the correct one.

while True :
    pwd = input("Enter password: ")

    if (pwd == "ADT"):
        print("correct password")
        break
    else:
        print("wrong password")