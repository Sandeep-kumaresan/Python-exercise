"""Create a class A and class B. Create class C that inherits from class A and B. 
use object of class C to inherit methods from both class A and class B"""
class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def prin(self):
        return self.name
class second:
    def agemat(self,age):
        if age<=18:
            return "student"
        else:
            return "adult"

class third(parent,second):
    print("Third class executed")

obj=third("Ajith",58)
print("The person",obj.prin(),"is ",obj.agemat(58))