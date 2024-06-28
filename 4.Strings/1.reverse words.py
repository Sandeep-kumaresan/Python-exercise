def list_inverse():
    word=input("Enter a word: ")
    word_new=word[::-1]
    print(word_new)

def list_loop():
    word=input("Enter a word: ")
    result = ""
    for i in word:
        result =i+result
    print(result)
    
def list_loop2():
    word=input("Enter a word: ")
    result = []
    for i in range(len(word)-1,-1,-1):
        result.append(word[i])
    print(result)
    
def reverse1():
    word=input("Enter a word: ")
    result=''.join(reversed(word))
    print(result)

def stack():
    word=input("Enter a word: ")
    for i in range(0,len(word)):
        word.push(stack)
