"""
Create a parent class called Polygon with an abstract method called
no_of_sides. Create Triangle and Pentagon Sub classes and implement the
abstract methods
"""

class Polygon():
    def no_of_sides(self):
        pass
class Triangle(Polygon):
    def no_of_sides(self):
        print("3 sides")

class Pentagon(Polygon):
    def no_of_sides(self):
        print("5 sides")


t=Triangle()
t.no_of_sides()
p=Pentagon()
p.no_of_sides()
