class circle:
    def __init__(self,radius):
        self.radius=radius
        self.pi=3.14
        
    def area(self):
        return self.pi*(self.radius**2)
    
    def perimeter(self):
        return 2*self.pi*self.radius
    
value=circle(4)
print("Area of Circle: ",value.area())
print("Perimeter of Circle: ",value.perimeter())
