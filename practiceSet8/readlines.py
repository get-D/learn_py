# Read the file and print all lines as a list using readlines().


with open("task.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line, end = "")