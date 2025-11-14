# Queue ADT
class Queue:
    def __init__(self): self.q=[]
    def enqueue(self,x): self.q.append(x)
    def dequeue(self): return self.q.pop(0) if self.q else "Underflow"
    def display(self): print(self.q)

q=Queue(); q.enqueue(10); q.enqueue(20); q.display()
