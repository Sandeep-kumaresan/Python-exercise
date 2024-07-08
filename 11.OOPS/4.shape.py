import math
class shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius
    
class triangle(shape):
    def __init__(self,breadth,height,a,c):
        self.breadth=breadth
        self.height=height
        self.a=a
        self.c=c
    def area(self):
        return 0.5*self.breadth*self.height
    def perimeter(self):
        return self.a+self.breadth+self.c
class square(shape):
    def __init__(self,side):
        self.side=side
    def perimeter(self):
        return 4*self.side
    def area(self):
        return self.side**2
r=5
cir=circle(r)
print("Area of circle",cir.area())
print("perimeter of circle",cir.perimeter())

breadth=6
height=4
a=5
c=7.5
tri=triangle(breadth,height,a,c)
print("Area of triangle",tri.area())
print("perimeter of triangle",tri.perimeter())

side=7
sq=square(side)
print("Area of square",sq.area())
print("perimeter of square",sq.perimeter())

        
        