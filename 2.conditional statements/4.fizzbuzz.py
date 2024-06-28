num=int(input("Enter number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Fizzbuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print("Not divisible by any number")