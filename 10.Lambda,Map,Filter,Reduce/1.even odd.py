"""Write a Python program to filter a list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]"""
dic=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even=list(filter(lambda x: (x % 2 == 0),dic))
odd = list(filter(lambda x:(x % 2== 1),dic))
print(even)
print(odd)