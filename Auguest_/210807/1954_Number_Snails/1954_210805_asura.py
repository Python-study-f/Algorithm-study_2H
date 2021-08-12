tc = int(input())

dx = [0,1,0,-1] # R,D,L,U / 방향성 우-하-상-좌
dy = [1,0,-1,0]

for T in range(1,tc+1):
    N = int(input())

    board = [[0]*N for _ in range(N)] # 보드판 생성
    x,y,dic = 0,0,0 # 시작점
    rst_cnt = N*N # 반복회수

    for i in range(rst_cnt):
        board[x][y] = i+1
        x,y = x + dx[dic], y + dy[dic]

        if not 0 <= x < N or not 0 <= y < N or board[x][y] != 0:
            x, y = x - dx[dic], y - dy[dic] # 범위에 벗어나서 다시 빼주고
            dic = (dic+1) %4 # 나눠주고
            x, y = x + dx[dic], y + dy[dic] # 더해주고

    print("#{}".format(T))
    for i in range(N):
        print(*board[i])