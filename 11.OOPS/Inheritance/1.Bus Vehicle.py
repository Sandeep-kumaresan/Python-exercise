"""Create a child class Bus that will inherit all of the 
variables and methods of the Vehicle class
"""
class Vehicle:
    def __init__(self,name,maxspeed,mileage):
        self.name=name
        self.maxspeed=maxspeed
        self.mileage=mileage
class Bus(Vehicle):
    pass

van=Bus("Volvo",80,20)
print("The bus name is ",van.name,",Maxspeed is ",van.maxspeed,",Mileage is ",van.mileage)