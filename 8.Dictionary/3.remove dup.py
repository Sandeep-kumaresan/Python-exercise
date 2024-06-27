"""Remove all duplicates from a given sentence
Input : Python is great and Java is also great
Output : is also Java Python and great
"""
def remove_duplicates(sentence):
    words = sentence.split()
    unique_words = {}
    for word in words:
        unique_words[word] = None
    sorted_unique_words = sorted(unique_words.keys())
    result = " ".join(sorted_unique_words)
    return result
sentence = "Python is great and Java is also great"
output = remove_duplicates(sentence)
print(output)
