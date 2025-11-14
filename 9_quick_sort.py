def qs(a):
    if len(a)<=1: return a
    p=a[0]
    left=[x for x in a[1:] if x<=p]
    right=[x for x in a[1:] if x>p]
    return qs(left)+[p]+qs(right)
print(qs([34,7,23,32,5,62]))
