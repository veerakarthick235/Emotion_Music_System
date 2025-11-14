class ListADT:
    def __init__(self): self.data=[]
    def insert(self,x): self.data.append(x)
    def delete(self,x):
        if x in self.data: self.data.remove(x)
    def display(self): print(self.data)

lst=ListADT(); lst.insert(10); lst.insert(20); lst.display()
