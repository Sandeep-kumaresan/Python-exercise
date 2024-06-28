set1={10,44,3,54,46}
min=list(set1)[0]
max=0
for i in set1:
    if i>max:
        max=i
    if i<min:
        min=i
print(min,max)