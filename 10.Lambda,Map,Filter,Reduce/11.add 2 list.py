""" Write a Python program to add two given lists using map and lambda.
[1, 2, 3]
[4, 5, 6]
Result: after adding two list
[5, 7, 9]
"""
lis=[1,2,3]
lis2=[4,5,6]
add=list(map(lambda x,y:x+y,lis,lis2))
print(add)