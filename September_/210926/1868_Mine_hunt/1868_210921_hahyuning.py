from collections import deque


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    a = [input() for _ in range(n)]
    bomb = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if a[i][j] == ".":
                cnt = 0
                for k in range(8):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == "*":
                        cnt += 1
                bomb[i][j] = cnt

    ans = 0
    for i in range(n):
        for j in range(n):
            if bomb[i][j] == 0:
                ans += 1
                bomb[i][j] = -1
                q = deque()
                q.append((i, j))

                while q:
                    x, y = q.popleft()
                    for k in range(8):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and bomb[nx][ny] != -1:
                            if bomb[nx][ny] == 0:
                                q.append((nx, ny))
                            bomb[nx][ny] = -1

    for i in range(n):
        for j in range(n):
            if bomb[i][j] > 0:
                ans += 1

    print("#{} {}".format(tc, ans))
