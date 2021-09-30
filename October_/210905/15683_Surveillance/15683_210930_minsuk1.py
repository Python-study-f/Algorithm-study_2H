n, m = map(int, input().split())
graph = []
total = 0
q = []
INF = int(1e9)
ans = INF
for i in range(n):
    tmp=list(map(int, input().split()))
    graph.append(tmp)
    for j in range(m):
        if tmp[j]!=0 and tmp[j]!=6:
            data+=1
            q.append([i,j,tmp[j]])


import copy
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
direction = [[], 
            [[0], [1], [2], [3]], 
            [[0, 1], [2, 3]], 
            [[0, 2], [2, 1], [1, 3], [3, 0]],
            [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]],
            [[0, 1, 2, 3]]]


def check(x,y,direction,tmp):
    for i in direction:
        nx = x
        ny = y
        while True:
            nx+=dx[i]
            ny+=dy[i]
            if 0<=nx<m and 0<=ny<n and tmp[nx][ny]!=6:
                if tmp[nx][ny]==0:
                    tmp[nx][ny]='#'
            else:
                break


def dfs(graph,cnt):
    global ans, total
    
    if cnt==total:
        count=0
        for i in graph:
            count+=i.count(0)
        ans=min(ans,count)
        return
    x,y,cctv=q[cnt]
    for i in direction[cctv]:
        tmp=copy.deepcopy(graph)
        check(x,y,i,tmp)
        dfs(tmp,cnt+1)
        

dfs(graph, 0)
print(ans)