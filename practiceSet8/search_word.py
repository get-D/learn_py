# Write a command-line utility search_word.py that takes two arguments:
# A filename
# A word to search and prints how many times the word appears in the file.

import sys

def search(word, string):
    return string.count(word)
    
if __name__ == "__main__":
    file = sys.argv[1]
    word = sys.argv[2]
    with open(file) as f:
        string = f.read()

    n = search(word, string)
    print(f"there are {n} occurences of '{word}' in the file.")