from collections import deque, defaultdict

def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])

    alpha = [False] * 26
    location = defaultdict(list)
    for i in range(m):
        for j in range(n):
            if board[i][j] not in ["*", "."]:
                location[ord(board[i][j]) - ord("A")].append((i, j))
                alpha[ord(board[i][j]) - ord("A")] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ans = ""
    while True:
        flag = False
        for i in range(26):
            if alpha[i]:
                sx, sy = location[i][0]
                ex, ey = location[i][1]
                q = deque()
                for k in range(4):
                    q.append((sx, sy, k))
                dist = [[-1] * n for _ in range(m)]
                dist[sx][sy] = 0

                while q:
                    x, y, dir = q.popleft()
                    if x == ex and y == ey:
                        break

                    for k in range(4):
                        if dir == k:
                            nx, ny = x + dx[k], y + dy[k]
                            if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == -1 and board[nx][ny] in [".", chr(i + ord("A"))]:
                                dist[nx][ny] = dist[x][y]
                                q.appendleft((nx, ny, k))
                        else:
                            nx, ny = x + dx[k], y + dy[k]
                            if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == -1 and board[nx][ny] in [".", chr(i + ord("A"))]:
                                dist[nx][ny] = dist[x][y] + 1
                                q.append((nx, ny, k))

                if dist[ex][ey] != -1 and dist[ex][ey] <= 2:
                    board[sx][sy] = "."
                    board[ex][ey] = "."
                    flag = True
                    ans += chr(i + ord("A"))
                    alpha[i] = False
        if not flag:
            break

    if len(ans) == len(location.keys()):
        return ans
    else:
        return "IMPOSSIBLE"

print(solution(3, 3, ["DBA", "C*A", "CDB"]))
print(solution(2, 4, ["NRYN", "ARYA"]))
print(solution(4, 4, [".ZI.", "M.**", "MZU.", ".IU."]))
print(solution(2, 2, ["AB", "BA"]))