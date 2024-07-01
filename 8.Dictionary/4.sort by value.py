a={3:"Mango",2:"Guava",5:"Grapes",4:"Peach",1:"Orange",6:"Apple",7:"Blackberry"}
sort=dict(sorted(a.items(), key=lambda item:item[1]))
print(sort)
sort2 = dict(sorted(a.items(), key=lambda item: item[1], reverse=True))
print(sort2)
