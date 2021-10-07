from itertools import combinations
from collections import deque
n = int(input())

data=[0]+list(map(int, input().split()))

graph={}
for i in range(n):
    tmp=list(map(int,input().split()))
    graph[i+1]=tmp[1:]


def check(data):
    visited = [0]*(n+1)
    visited[list(data)[0]] = 1
    q = deque(graph[list(data)[0]])
    while q:
        x = q.popleft()
        if x in data and not visited[x]:
            visited[x] = 1
            for i in graph[x]:
                q.append(i)
    
    isFlag=True
    for i in data:
        if visited[i] != True:
            isFlag=False
    return isFlag


def sol(a,b):
    x=sum([data[i] for i in a])
    y=sum([data[i] for i in b])
    return abs(x-y)


ans=int(1e9)
for i in range(1,n//2+1):
    for j in combinations(list(range(1,n+1)), i):
        a=set(j)
        b=set(range(1,n+1))-a
        if check(a) and check(b):
            ans=min(ans, sol(a, b))


if ans==int(1e9):
    print(-1)
else:
    print(ans)