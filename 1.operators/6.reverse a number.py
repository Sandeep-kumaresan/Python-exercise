#reverse a number
n=int(input("Enter number: "))
reverse=0
while n>0:
    a=n%10
    reverse=reverse*10+a
    n=n//10
print(reverse)
"""
n = input("Enter number: ")
b = n[::-1]
print(b)

"""