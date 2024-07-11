"""Write a Python program to extract year, month, date and time using Lambda."""
import datetime
now=datetime.datetime.now()
print(now)
year= lambda x : x.year
month= lambda x : x.month
date= lambda x : x.day
time= lambda x: x.time()
print(year(now))
print(month(now))
print(date(now))
print(time(now))
