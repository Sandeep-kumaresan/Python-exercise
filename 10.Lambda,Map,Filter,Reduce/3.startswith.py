"""Write a Python program to find if a given string starts with a given character using Lambda."""
starts_with = lambda string, char: string.startswith(char)

string = input("Enter a string: ")
char = input("Enter the character to check: ")

if starts_with(string, char):
    print(f'The string "{string}" starts with the character "{char}".')
else:
    print(f'The string "{string}" does not start with the character "{char}".')
