def decorator1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decorator2(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decorator1
@decorator2
def num1():
   return 10

@decorator2
@decorator1
def num2():
   return 10

print(num1())
print(num2())