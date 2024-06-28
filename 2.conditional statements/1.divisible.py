num=int(input("Enter number: "))
if num % 2 == 0 and num % 3==0 and num % 4 == 0:
    print("Divisible by 2,3,4")
elif num % 2 == 0:
    print("Divisible by 2")
elif num % 3 == 0:
    print("Divisible by 3")
elif num % 4 == 0:
    print("Divisible by 4")