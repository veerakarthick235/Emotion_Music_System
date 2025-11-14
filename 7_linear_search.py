def linear_search(a,k):
    for i,v in enumerate(a):
        if v==k: return i
    return -1
print(linear_search([10,30,50,70,90],70))
