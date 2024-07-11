"""Calculate the mean values of the elements from input list
[2, 4, 6, 9, 11]
"""
from functools import reduce
def mea(lis):
    return reduce(lambda a,b: a+b,lis)/len(lis)
lis=[2,4,5,9,11]
print(mea(lis))