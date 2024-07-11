"""Write a Python program to count the even and odd numbers in a given array of integers using Lambda."""
lis=[1,2,3,4,5,6,7,8,9]
count1=len(list(filter(lambda x : x%2==0,lis)))
count2=len(list(filter(lambda x : x%2==1,lis)))
print(count1)
print(count2)