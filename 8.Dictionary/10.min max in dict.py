lis={'a':2,'b':3,'c':4,'d':0}
maxitem=next(iter(lis))
minitem=next(iter(lis))
for i in lis:
    if lis[maxitem] < lis[i]:
        maxitem = i
    if lis[minitem] > lis[i]:
        minitem = i
print(maxitem)
print(minitem)