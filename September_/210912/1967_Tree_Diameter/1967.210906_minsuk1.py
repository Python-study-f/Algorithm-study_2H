import sys
sys.setrecursionlimit(10**9)
n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    
result1 = [0 for _ in range(n+1)]

def dfs(x,result):
    for a,b in graph[x]:
        if result[a] == 0:
            result[a] = result[x] + b
            dfs(a,result)
            
            
dfs(1,result1)
result1[1] = 0

tmp = 0
index = 0
for i in range(len(result1)):
    if tmp<result1[i]:
        tmp = result1[i]
        index = i
        
result2 = [0 for _ in range(n+1)]
dfs(index,result2)
result2[index] = 0
print(max(result2))