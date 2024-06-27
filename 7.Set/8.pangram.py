def pangram(input_string):
    alpha = set("abcdefghijklmnopqrstuvwxyz")
    found = set()
    for char in input_string.lower():
        if char in alpha:
            found.add(char)
    if alpha == found:
        return "Accepted"
    else:
        return "Not Accepted"
    
input_string="The quick brown fox jumps over the lazy dog"
result = pangram(input_string)
print(result)