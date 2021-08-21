import heapq; import sys; input=sys.stdin.readline
n,l = map(int, input().split())
INF=int(1e9)
lines = []
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
visited=[False]*l

for i in range(l):
    tmp = list(map(int, input().split()))
    line=tmp[:-1]
    lines.append(line)
    
    for j in line:
        graph[j].append(i)

start, end = map(int, input().split())

def sol(start,end,dist):
    if start==end:
        return 0
    
    q = []
    distance[start] = 0
    heapq.heappush(q, (0,start))
    
    while q:
        dist,now=heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            if visited[i]:
                continue
            
            visited[i]=True
            
            for next in lines[i]:
                if distance[next] > dist+1:
                    distance[next] = dist+1
                    heapq.heappush(q, (dist+1,next))
                    
                    if next==end:
                        return dist
    
    return -1

print(sol(start,end,distance))