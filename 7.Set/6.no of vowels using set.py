"""Input : Hello World
Output : No. of vowels : 3"""

vowels={"a","e","i","o","u","A","E","I","O","U"}
word=input("Enter word: ")
count=0
for i in word:
    if i in vowels:
        count+=1
print("No. of vowels: ",count)