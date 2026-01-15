# Open notes.txt , read its content, and print it to the console.

try:
    with open("notes.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("notes.txt does not exist!")