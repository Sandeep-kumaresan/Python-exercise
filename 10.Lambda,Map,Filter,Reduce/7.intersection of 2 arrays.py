"""Write a Python program to find the intersection of two given arrays using Lambda."""
lis1=[1,2,3,4,5,6]
lis2=[3,2,5,8,9,0]
result = list(filter(lambda x : x in lis1,lis2))
print(result)
