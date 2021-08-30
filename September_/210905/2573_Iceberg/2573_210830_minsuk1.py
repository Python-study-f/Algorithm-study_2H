import copy
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def check():
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                return False
    return True


def bfs(i, j):
    q = deque()
    q.append([i,j])
    visit = [[0] * m for i in range(n)]
    visit[i][j] = 1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0 and temp[nx][ny] != 0:
                temp[nx][ny] = 0
                visit[nx][ny] = 1
                q.append([nx, ny])
                
                
def remove(i, j):
    cnt = 0
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < n and 0 <= ny < m and tmp[nx][ny] == 0:
            cnt += 1
    return cnt



ans = 1
while True:
    
    if check():
        print(0)
        break

    tmp = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if tmp[i][j] != 0:
                temp = graph[i][j] - remove(i,j)
                graph[i][j] = temp if temp>0 else 0
            
    
    temp = copy.deepcopy(graph)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] != 0:
                temp[i][j] = 0
                bfs(i, j)
                cnt += 1
                
    if cnt>1:
        print(ans)
        break
        
    ans+=1