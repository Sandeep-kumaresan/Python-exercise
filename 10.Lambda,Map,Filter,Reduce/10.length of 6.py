"""Write a Python program to filter a given list to determine if the values in the list have a length of 6 using Lambda."""
lis=["asdfgq","asdf","sdkfoo","er6f"]
length=list(filter(lambda x : len(x)==6,lis))
print(length)