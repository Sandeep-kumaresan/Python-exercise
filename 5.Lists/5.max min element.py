lis=[100,1000,100000,154,8451]
min=lis[0]
max=lis[0]
for i in lis:
    if i>min:
        min=i
    if i<max:
        max=i
print(min,max)