from collections import deque

def solution(n, edge):
    
    graph=[[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    q = deque([[1, 0]]) 
    visited = [-1]*(n+1)
    while q:
        idx, depth = q.popleft()
        visited[idx] = depth
        for i in graph[idx]:
            if visited[i]==-1:
                visited[i] = 0
                q.append([i, depth+1])
        depth += 1
    return visited.count(max(visited))