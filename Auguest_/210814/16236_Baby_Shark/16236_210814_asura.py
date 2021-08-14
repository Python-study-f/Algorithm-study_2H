# N,N 크기 / M 마리 물고기 / 초기 아기상어 1마리
# case1. 자기보다 작은 물고기 먹고 지나감 / case2. 자기랑 동급은 그냥 지나감 / case3. 자기보다 크면 지나가지도 못함
# 상하좌우, 최단 => BFS

# 결국 블로그를 통해 해결.
# https://pg-wonie.tistory.com/26
# https://dailyheumsi.tistory.com/59
# https://imksh.com/29

from collections import deque

def bfs(x,y):
    dq, visited = deque([(x,y)]), {(x, y)}
    shark, eat, time = 2, 0, 0
    flag = False # 현재 상태에서 물고기를 먹은 경우,
                 # for _ in range(size) 구문을 진행하지 않기 위한 flag다.
    ans = 0

    while dq:
        size = len(dq)

        # 위 그리고 왼쪽을 더 우선시 가야하기 때문에, dq 소팅
        dq = deque(sorted(dq))

        for _ in range(size):
            x,y = dq.popleft()

            if data[x][y] != 0 and data[x][y] < shark:
                data[x][y] = 0
                eat += 1

                # 아기 상어의 크기 만큼 먹었다면, 아기 상어의 크기를 +1 해줘야한다.
                if eat == shark:
                    shark += 1
                    eat = 0

                # 먹고 난 뒤, 현재 위치를 기준으로 다시 근처를 탐색
                dq, visited = deque(), {(x,y)}
                flag = True

                ans = time

            for dic in range(4):
                nx, ny = x + dx[dic], y + dy[dic]

                if 0 <= nx < N and 0 <= ny < N and (nx,ny) not in visited:
                    if data[nx][ny] <= shark:
                        dq.append((nx,ny))
                        visited.add((nx,ny))

            if flag:
                flag = False
                break

        time += 1
    return ans

dx = [0,0,-1,1]
dy = [-1,1,0,0]

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]

shark_x,shark_y = None, None


# 1. 초기 상어의 위치 체크한 후, 해당 자리에 빈 공간으로 체크
for i in range(N):
    for j in range(N):
        if data[i][j] == 9:
            shark_x,shark_y = i,j
            data[i][j] = 0

# 2. 시작점에서 bfs 때린다.
print(bfs(shark_x,shark_y))