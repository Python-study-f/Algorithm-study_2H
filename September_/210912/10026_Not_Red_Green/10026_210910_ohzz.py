# 적록색약 10026 백준

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

arr = [list(input()) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def check_color(v, checkValue, case):
    if case == 1:
        if v == checkValue:
            return True
        return False
    else:
        if checkValue == "R" or checkValue == "G":
            if v == "R" or v == "G":
                return True
            return False
        else:
            if v == checkValue:
                return True
            return False


def bfs(i, j, value, case):
    q = deque()
    q.append([i, j])
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < n
                and visited[nx][ny] == False
                and check_color_normal(arr[nx][ny], value, case)
            ):

                visited[nx][ny] = True
                q.append([nx, ny])


T = 0
res = []
cnt = 0
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            visited[i][j] = True
            bfs(i, j, arr[i][j], 1)
            cnt += 1

res.append(cnt)

cnt = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            visited[i][j] = True
            bfs(i, j, arr[i][j], 2)
            cnt += 1
res.append(cnt)

print(res[0], res[1])
