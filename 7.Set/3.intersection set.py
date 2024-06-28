ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
set1=set(ar1)
set2=set(ar2)
set3=set(ar3)
result=list(set1.intersection(set2,set3))
print(result)