inp=input()
lis=inp.split()
inp2=[]
for i in lis:
    if i not in inp2:
        inp2.append(i)
inp3=" ".join(inp2)
print(inp3)