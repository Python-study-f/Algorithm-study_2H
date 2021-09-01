# 빙산 2573 백준

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

res = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def melting_ice():
    tmp_area = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):

            if area[i][j] != 0:
                # 네 방향 검사해서 0인 곳 카운트 세서 tmp_area에 넣어주기
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < n and 0 <= ny < m and area[nx][ny] == 0:
                        cnt += 1
                tmp_area[i][j] = cnt

    # 원래 값에서 tmp_area 거 빼면 다음 년도 ice가 남음 0보다 작으면 0으로 선언
    for i in range(n):
        for j in range(m):
            if (area[i][j] - tmp_area[i][j]) > 0:
                area[i][j] = area[i][j] - tmp_area[i][j]
            else:
                area[i][j] = 0


# 분리된 Part
def bfs(i, j):
    q = deque()
    q.append([i, j])

    visited[i][j] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and area[nx][ny] != 0:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])


while True:
    part = 0
    # 방문한 걸 바깥에서 비교해줘야함 이것때문에 답이 안나왔음
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if area[i][j] != 0 and visited[i][j] == 0:
                part += 1
                bfs(i, j)
    if part == 0:
        print(0)
        break

    if part >= 2:
        print(res)
        break

    res += 1

    melting_ice()
