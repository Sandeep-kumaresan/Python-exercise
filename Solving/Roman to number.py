roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
i="MDC"
r=0
for n in range(len(i)):
    if roman[i[n]] <roman[i[n]]+1 and roman[i[n]] < len(i):
        r-=roman[i[n]]
    else:
        r+=roman[i[n]]
print(r)