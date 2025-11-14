def bs(a,k):
    l,h=0,len(a)-1
    while l<=h:
        m=(l+h)//2
        if a[m]==k: return m
        if k<a[m]: h=m-1
        else: l=m+1
    return -1
print(bs([10,20,30,40,50],40))
