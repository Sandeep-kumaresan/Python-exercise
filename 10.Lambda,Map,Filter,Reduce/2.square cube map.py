"""Write a Python program to square and cube every number in a given list of integers using Lambda.

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"""
lis=[1,2,3,4,5,6,7,8,9,10]
square=list(map(lambda x:x**2,lis))
cube=list(map(lambda x:x**3,lis))
print(square)
print(cube)