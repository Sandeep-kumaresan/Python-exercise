lis=[1,2,3,3,2,1,2]
n=int(input("Enter element to search:"))
count=0
for i in lis:
    if i == n:
        count+=1
print(count)