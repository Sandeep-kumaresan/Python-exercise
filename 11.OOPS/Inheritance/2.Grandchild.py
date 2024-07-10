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
