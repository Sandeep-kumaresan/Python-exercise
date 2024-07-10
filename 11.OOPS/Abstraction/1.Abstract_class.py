from abc import ABC
class Car(ABC):
    def mileage(self):
        pass
class Suzuki(Car):
    def mileage(self):
        print("Mileage is 35kmpl")

class Honda(Car):
    def mileage(self):
        print("Mileage is 40kmpl")

class TVS(Car):
    def mileage(self):
        print("Mileage is 45kmpl")

s=Suzuki()
s.mileage()
h=Honda()
h.mileage()
t=TVS()
t.mileage()
