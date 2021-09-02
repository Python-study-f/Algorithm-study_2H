from collections import deque

# 1. 블록 나누기
def bfs(x, y, a, visited, num):
    n = len(a)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((x, y))
    visited[x][y] = True

    min_x, min_y, max_x, max_y = n - 1, n - 1, 0, 0

    while q:
        x, y = q.popleft()
        min_x, min_y = min(min_x, x), min(min_y, y)
        max_x, max_y = max(max_x, x), max(max_y, y)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if a[nx][ny] == num:
                    q.append((nx, ny))

    res = [[0] * (max_y - min_y + 1) for _ in range(max_x - min_x + 1)]
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            res[i - min_x][j - min_y] = a[i][j]

    return res, visited

# 블록 회전
def rotation(a):
    n = len(a)
    m = len(a[0])

    b = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            b[j][n - i - 1] = a[i][j]
    return b

# 퍼즐 맞추기
def match(puzzle, blank):

    res = [False] * len(puzzle)
    blank_check = [False] * len(blank)

    for k, p in enumerate(puzzle):
        for l, b in enumerate(blank):
            if blank_check[l]:
                continue

            match_check = False
            for _ in range(4):
                p = rotation(p)

                if len(b) != len(p) or len(b[0]) != len(p[0]):
                    continue

                ch = False
                for i in range(len(b)):
                    for j in range(len(b[0])):
                        tmp = p[i][j] + b[i][j]
                        if tmp != 1:
                            ch = True
                            break
                    if ch:
                        break
                if not ch:
                    match_check = True
            if match_check:
                res[k] = True
                blank_check[l] = True
                break
    return res

# 메인
def solution(game_board, table):
    n = len(table)

    # 블록 나누기
    puzzle = []
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not visited[i][j]:
                res, visited = bfs(i, j, table, visited, 1)
                puzzle.append(res)

    blank = []
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0 and not visited[i][j]:
                res, visited = bfs(i, j, game_board, visited, 0)
                blank.append(res)

    # 퍼즐 맞추기
    res = match(puzzle, blank)

    ans = 0
    for k in range(len(res)):
        if res[k]:
            p = puzzle[k]
            for i in range(len(p)):
                for j in range(len(p[0])):
                    if p[i][j] == 1:
                        ans += 1
    return ans