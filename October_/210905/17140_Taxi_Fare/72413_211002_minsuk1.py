#시간초과
def solution(n, s, a, b, fares):
    INF=int(1e9)
    data=[[INF]*(n+1) for _ in range(n+1)]
    
    for fare in fares:
        data[fare[0]][fare[1]]=fare[2]
        data[fare[1]][fare[0]]=fare[2]
    
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j: data[i][j]=0
                
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                data[i][j]=min(data[i][j], data[i][k]+data[k][j])
    
    ans=INF
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                ans=min(ans, data[s][k]+data[k][a]+data[k][b])
        
    return ans



import heapq; INF=int(1e9)
def dijstra(start,end,n):
    distance=[INF]*(n+1)
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    
    return distance[end]


def solution(n, s, a, b, fares):
    global graph, length
    
    answer = INF
    graph = [[] for _ in range(n+1)]
   
    
    for i, j, cost in fares:
        graph[i].append([j, cost])
        graph[j].append([i, cost])
            
    for i in range(1, n+1):
        answer = min(answer, dijstra(s,i,n)+dijstra(i,a,n)+dijstra(i,b,n))
        
    return answer