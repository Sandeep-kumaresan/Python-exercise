class stack:
    def __init__(self):
        self.st=[]
    def push(self,i):
        self.st.append(i)
    def pop1(self):
        if not len(self.st) == 0:
            return self.st.pop()
        else:
            print("Error,Stack is empty")
            return None
    def peek(self):
        if not len(self.st) == 0:
            return self.st[-1]
        else:
            return "stack empty"

stack1= stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
print(stack1.st)
stack1.pop1()
print(stack1.st)
print(stack1.peek())