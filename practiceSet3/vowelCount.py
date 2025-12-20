# Write a program that counts how many vowels are in a given string

sentence = "Coding in Python is fun"

sum = 0
vowels = "aeiou"

for char in sentence.lower():
    if (char in vowels):
        sum += 1

print(f"there are {sum} in the sentence ")