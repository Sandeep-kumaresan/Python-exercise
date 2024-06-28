lis={1:2,2:3,5:8,4:9}
sum=[]
for key in lis:
    sum.append(key+lis[key])
print(list(sum))