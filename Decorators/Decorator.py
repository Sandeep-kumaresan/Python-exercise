def decorator(func):
    def inner(a,b):
        print("before operation")

        func(a,b)

        print("after operation")

    return inner

def add(x,y):
    print("Addition is :",x+y)

@decorator
def subtract(x,y):
    print("Subtraction is: ",x-y)

add_numbers=decorator(add)
add_numbers(10,20)
subtract(30,10)

