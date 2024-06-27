a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
aa=set(a)
bb=set(b)
ele=aa.intersection(bb)
for i in ele:
    if i in aa:
        print(True)
    else:
        print(False)