"""Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
"""
lis=[1,-2,-6,4,-7,3]
rearrange=lambda lis: [x for x in lis if x< 0]+[x for x in lis if x>=0]
arr2=rearrange(lis)
print(arr2)