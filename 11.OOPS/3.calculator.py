class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def subtract(self):
        return self.a-self.b
    def multiply(self):
        return self.a*self.b
    def divide(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a/self.b
op=calculator(5,0)
print("add: ",op.add())
print("subtract: ",op.subtract())
print("multiply: ",op.multiply())
print("divide: ",op.divide())