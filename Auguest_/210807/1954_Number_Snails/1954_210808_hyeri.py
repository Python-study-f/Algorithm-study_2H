T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for test_case in range(1,T+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)] 
    nx,ny,dir = 0,0,0 
    num = 1
    while num <= N*N:
        arr[nx][ny] = num
        tx, ty = nx + dx[dir], ny + dy[dir]
        if tx < 0 or tx >= N or ty < 0 or ty >= N or arr[tx][ty] != 0 :
            dir += 1
            if dir > 3:
                dir = 0
        nx, ny = nx + dx[dir], ny + dy[dir]
        num += 1
        
    print("#{}".format(test_case))
    for i in range(N):
        print(*arr[i])
