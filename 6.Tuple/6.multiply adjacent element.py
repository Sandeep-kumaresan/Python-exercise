li=(1, 5, 7, 8, 10)
#(5, 35, 56, 80)
li2=list(li)
li3=[]
for i in range(len(li2)+1):
    if i <len(li2)-1:
        j=li2[i]*li2[i+1]
        li3.append(j)
li4=tuple(li3)
print(li4)