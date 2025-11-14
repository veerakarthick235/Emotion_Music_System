def add_poly(p1,p2):
    size=max(len(p1),len(p2))
    res=[0]*size
    for i in range(size):
        res[i]=(p1[i] if i<len(p1) else 0)+(p2[i] if i<len(p2) else 0)
    return res

print(add_poly([5,0,10,6],[1,2,4]))
