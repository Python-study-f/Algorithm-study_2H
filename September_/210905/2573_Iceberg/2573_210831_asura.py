from collections import deque
import  copy

dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 입력
N,M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
year = 0

def check():
    for i in range(N):
        for j in range(M):
            if data[i][j] != 0:
                return False
    return True

def zero(x,y):
    cnt = 0

    for i in range(4):
        nx,ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == 0:
            cnt += 1
    return cnt

def bfs(x,y):
    dq = deque()
    dq.append((x,y))

    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1

    while dq:
        x,y = dq.popleft()

        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and tmp[nx][ny] != 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                tmp[nx][ny] = 0
                dq.append((nx,ny))

while True:
    year += 1

    # 다 녹는다면
    if check():
        print("0")
        break

    tmp = [[0] * M for _ in range(N)]

    # 해수면 값 조정
    for a in range(N):
        for b in range(M):
            if data[a][b] != 0:
                count = zero(a,b)
                val = data[a][b] - count

                # 0보다 크면 val, 작으면 그냥 0으로 초기화
                if val >= 0 :
                    tmp[a][b] = val
                else:
                    tmp[a][b] = 0

    # 해수면 값 반영
    data = copy.deepcopy(tmp)

    # 덩어리 체크
    dong = 0
    for a in range(N):
        for b in range(M):
            if tmp[a][b] != 0:
                dong += 1
                bfs(a,b)

    if dong >= 2:
        print(year)
        break



