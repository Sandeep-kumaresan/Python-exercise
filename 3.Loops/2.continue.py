num=int(input("Enter a number: "))
for i in range(num+1):
    if i % 10 == 0:
        continue
    else:
        print(i)