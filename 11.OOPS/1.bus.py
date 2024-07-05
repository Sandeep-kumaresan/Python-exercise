class Vehicle:
    def __init__(self,name,wheel,fuel):
        self.name=name
        self.wheel=wheel
        self.fuel=fuel
    
    def info(self):
        return self.name,self.wheel,self.fuel
        
    def ignite(self):
        return "Engine started"

class Bus(Vehicle):
    def __init__(self, name, wheel, fuel,year):
        super().__init__(name, wheel, fuel)
        self.year=year
        
    def businfo(self):
        return "the bus info is",self.info(),self.year
    
myvehicle=Bus("Ashok Leyland",4,"petrol",2016)
print(myvehicle.businfo())
print(myvehicle.info())
print(myvehicle.ignite())
     