"""Create a parent class A, Child class B, Grand Child class C. 
Use Child C object to access the instance variable and methods of 
class A"""
class parent:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
class child(parent):
    pass
class grandchild(child):
    pass
family=grandchild("Samurai",209)
print("The name is ",family.name,"with roll number ",family.roll)
