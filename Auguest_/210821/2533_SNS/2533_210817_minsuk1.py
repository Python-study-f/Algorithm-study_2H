import sys; input=sys.stdin.readline; sys.setrecursionlimit(10000) 
n=int(input())
parent=[0]*(n+1)
visited=[0]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
tmp=set()
def dfs(x,depth):
    visited[x]=True
    for node in graph[x]:
        if visited[node]:
            continue
        tmp.add(x)
        parent[node]=x
        dfs(node,depth+1)

        
dfs(1,0)


for i in graph[1]:
    if i not in tmp:
        ans+=1
        
print(ans)