class queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,i):
        return self.items.append(i)
    def dequeue(self):
        if not len(self.items) == 0:
            return self.items.pop(0)
        else:
            return "Queue empty"
que=queue()
que.enqueue(1)
que.enqueue(2)
que.enqueue(4)
que.enqueue(3)
print(que.items)
select=que.dequeue()
print("dequeued item:",select)
print(que.items)