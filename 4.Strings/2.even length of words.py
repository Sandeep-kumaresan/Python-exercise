inp=input("Enter String: ")
inp2=inp.split()
for i in inp2:
    if len(i) % 2 == 0:
        print(i)
