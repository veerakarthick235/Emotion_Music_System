class Node:
    def __init__(self,k): self.key=k; self.left=None; self.right=None

def insert(r,k):
    if not r: return Node(k)
    if k<r.key: r.left=insert(r.left,k)
    else: r.right=insert(r.right,k)
    return r

def inorder(r):
    if r:
        inorder(r.left); print(r.key,end=" "); inorder(r.right)

root=None
for k in [50,30,20,40,70,60,80]: root=insert(root,k)
inorder(root)
