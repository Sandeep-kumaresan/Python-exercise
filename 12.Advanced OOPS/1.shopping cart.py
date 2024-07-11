class shopping:
    def __init__(self):
        self.items=[]
    def add(self,item,qty):
        ab=(item,qty)
        self.items.append(ab)

    def rem(self,item):
        for i in self.items:
            if i[0] == item:
                self.items.remove(i)
                break
    def calculate(self):
        total=0
        for i in self.items:
            total+=i[1]
        return total

shop=shopping()
shop.add("apple",20)
shop.add("berry",30)
shop.add("cherry",40)
print(shop.items)
shop.rem("apple")
print(shop.items)
print(shop.calculate())