g={'A':['B','C'],'B':['D','E'],'C':['F'],'D':[],'E':[],'F':[]}
def dfs(n,v=set()):
    print(n,end=" "); v.add(n)
    for x in g[n]:
        if x not in v: dfs(x,v)
dfs('A')
