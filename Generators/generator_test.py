def simpleGenerator():
    yield 1
    yield 2
    yield 3
for value in simpleGenerator():
    print(value)

x = simpleGenerator()
print("1st" , next(x))
print("2nd" , next(x))
print("3nd" , next(x))
generator_exp = (i*5 for i in range(5) if i%2 == 0)
for i in generator_exp:
    print(i)

#for i in range(5):
    #if i%2 == 0:
        #print(i*5)

def fib(num):
    a,b=0,1
    while a < num:
        yield a
        a,b=b,a+b


x=fib(10)
print(next(x))
print(next(x))
print(next(x))