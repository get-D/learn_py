# Write a small script count_lines.py that takes a filename as input and prints how many lines are in the file.


import sys

def count(file):
    with open(file) as f:
        return len(f.readlines())
    
if __name__ == "__main__":
    file = sys.argv[1]
    lineNum = count(file)
    print(f"there are {lineNum} lines in {file}.")
