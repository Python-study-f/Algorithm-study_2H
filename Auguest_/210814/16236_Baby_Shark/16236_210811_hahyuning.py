from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, size):
    # 먹을 수 있는 물고기까지의 거리와 위치 정보를 담은 배열
    ans = []
    d = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    d[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == -1:
                move = False
                eat = False
                # 이동하려는 곳이 빈 칸인 경우
                if a[nx][ny] == 0:
                    move = True
                # 이동하려는 곳의 물고기를 먹을 수 있는 경우
                elif a[nx][ny] < size:
                    move = True
                    eat = True
                # 이동할 수 있지만 물고기를 못먹는 경우
                elif a[nx][ny] == size:
                    move = True

                if move == True:
                    q.append((nx, ny))
                    d[nx][ny] = d[x][y] + 1
                    # 먹을 수 있는 물고기의 좌표 기록
                    if eat == True:
                        ans.append((d[nx][ny], nx, ny))

    if not ans:
        return (-1, -1, -1)
    ans.sort()
    return ans[0]

n = int(input())
a = [list(map(int, input().rstrip().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 상어의 위치
sx, sy = 0, 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 9:
            sx, sy = i, j
            a[i][j] = 0

ans = 0 # 걸린 시간
s_size = 2 # 상어의 크기
num = 0 # 먹은 물고기의 개수

while True:
    p = bfs(sx, sy, s_size)
    # 먹을 수 있는 물고기가 없다면 break
    if p[0] == -1:
        break

    # 먹을 수 있으면서 가장 가까운 물고기까지의 거리, 물고기의 위치
    dist, nx, ny = p
    a[nx][ny] = 0
    ans += dist
    num += 1
    sx, sy = nx, ny

    # 상어의 크기가 먹은 물고기의 수와 같아진 경우
    if s_size == num:
        s_size += 1
        eat_num = 0

print(ans)