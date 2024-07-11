"""
Create a parent class and child class. Create a function called
print in both the classes to observe method overriding
"""

class Vehicle:
    def print(self):
        print("I am vehicle")

class Car(Vehicle):
    def print(self):
        print("I am Car")

ab=Car()
ab.print()
