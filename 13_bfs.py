from collections import deque
g={'A':['B','C'],'B':['D','E'],'C':['F'],'D':[],'E':[],'F':[]}
def bfs(s):
    vis=set(); q=deque([s])
    while q:
        n=q.popleft()
        if n not in vis:
            print(n,end=" "); vis.add(n); q.extend(g[n])
bfs('A')
