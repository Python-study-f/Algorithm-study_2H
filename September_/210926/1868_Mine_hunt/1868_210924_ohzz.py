# 파핑파핑 지뢰찾기 1868 SW expert

from collections import deque

T = int(input())

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]


def check_mine(x, y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == ".":
                continue
            elif board[nx][ny] == "*":
                return False
    return True


def bfs(xx, yy):
    q = deque()
    q.append((xx, yy))
    while q:
        x, y = q.popleft()
        board[x][y] = "C"

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == ".":
                    if not check_mine(nx, ny):
                        board[nx][ny] = "C"
                    else:
                        board[nx][ny] = "C"
                        q.append((nx, ny))


for t in range(1, T + 1):
    n = int(input())
    board = []
    for i in range(n):
        board.append(list(input()))

    click = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] == ".":
                if check_mine(i, j):
                    bfs(i, j)
                    click += 1

    for i in range(n):
        for j in range(n):
            if board[i][j] == ".":
                click += 1

    print(f"#{t} {click}")
