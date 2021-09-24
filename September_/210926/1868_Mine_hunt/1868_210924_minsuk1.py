from collections import deque
dx=[-1, -1, -1, 0, 1, 1, 1, 0]
dy=[-1, 0, 1, 1, 1, 0, -1, -1]


def check(x,y):
    global cnt
    tmp = []
    isFlag=True
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == '.':
                tmp.append((nx, ny))
            elif graph[nx][ny] == '*':
                isFlag=False
                break
    
    if isFlag: 
        graph[x][y] = '0'
        cnt += 1
        bfs(tmp)


def bfs(tmp):
    q = deque(tmp)
    while q:
        x,y = q.popleft()
        graph[x][y]='0'
        next_tmp=[]
        isFlag=True
        for i in range(8): 
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == '.':
                    next_tmp.append((nx, ny))
                elif graph[nx][ny] == '*':
                    isFlag=False
                    break
        if isFlag:
            bfs(next_tmp)


def last():
    global cnt
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '.':
                cnt += 1



t=int(input())
for k in range(1,t+1):
    n=int(input())
    graph=[]
    for i in range(n):
        graph.append(list(input().strip()))
        
    cnt=0
    for i in range(n):
        for j in range(n):
            if graph[i][j]=='.':
                check(i,j)
    last()
    
    print('#{} {}'.format(t, cnt))
