"""Write a Python program to check whether a given string is a number or not using Lambda."""
num=input("Enter value: ")
n=lambda x: x.replace(".","").isdigit()
print(n(num))