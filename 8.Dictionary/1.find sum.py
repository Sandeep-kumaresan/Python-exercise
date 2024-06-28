"""Find the sum of all items 
Input : {‘a’: 100, ‘b’:200, ‘c’:300}
Output : 600"""
dic={'a': 100, 'b':200, 'c':300}
res=dic.values()
print(res)
sum=0
for i in res:
    sum+=i
print(sum)