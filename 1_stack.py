# Stack ADT
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        return self.stack.pop() if self.stack else "Underflow"
    def display(self):
        print(self.stack)

s=Stack(); s.push(10); s.push(20); s.display()
