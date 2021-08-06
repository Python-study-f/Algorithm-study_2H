t=int(input())
for _ in range(t):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    n=int(input())
    data = [[0]*n for _ in range(n)]
    
    x,y=0,0
    dir=0
    data[x][y]=1
    nx,ny=0,0
    for i in range(2,n**2+1):
        nx+=dx[dir]
        ny+=dy[dir]
        data[nx][ny]=i

        if 0<=nx+dx[dir]<n and 0<=ny+dy[dir]<n and not data[nx+dx[dir]][ny+dy[dir]]:
            continue
        if dir!=3:
            dir+=1
        else:
            dir=0
    
    for i in data:
        print(*i)