list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]
li1=set(list1)
li2=set(list2)
result=li1.difference(li2)
re2=list(result)
re2.sort()
print(re2)