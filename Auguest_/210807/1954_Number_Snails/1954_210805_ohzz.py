# 달팽이 숫자 1954 SW expert

t = int(input())

# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def rotate(dir):
    dir = (dir + 1) % 4
    return dir


def checkIndex(x, y, n):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


def dfs(d, L, n, x, y, dir, board):
    if d == (L + 1):
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
            print()
        return
    else:
        board[x][y] = d
        next_x = x + dx[dir]
        next_y = y + dy[dir]

        if checkIndex(next_x, next_y, n) and board[next_x][next_y] == 0:
            dfs(d + 1, L, n, next_x, next_y, dir, board)
        else:
            dir = rotate(dir)
            next_x = x + dx[dir]
            next_y = y + dy[dir]
            dfs(d + 1, L, n, next_x, next_y, dir, board)


for i in range(t):
    n = int(input())
    board = [[0] * n for _ in range(n)]
    print(f"#{i + 1}")
    dfs(1, n * n, n, 0, 0, 0, board)
