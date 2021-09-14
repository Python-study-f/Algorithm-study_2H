import heapq

def solution(N,road,K):
    INF = int(1e9) 
    graph = [[] for _ in range(N+1)]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    distance = [INF] * (N+ 1)
    
#---------------------------------------------
    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    while q: 
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

#---------------------------------------------
    count=0
    for i in distance:
        if i<=K:
            count+=1
    
    
    return count