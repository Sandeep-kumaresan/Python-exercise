"""Input : ABeeIghiObhkUul
Output : Accepted
All vowels are present
"""
def contains_all_vowels(input_string):
    vowels = set("aeiou")
    found_vowels = set()
    for char in input_string.lower():
        if char in vowels:
            found_vowels.add(char)
    if vowels == found_vowels:
        return "Accepted"
    else:
        return "Not Accepted"
input_string = "AIeoU"
result = contains_all_vowels(input_string)
print(result)
