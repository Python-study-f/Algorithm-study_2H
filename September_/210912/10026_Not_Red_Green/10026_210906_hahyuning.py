from collections import deque
import sys
input = sys.stdin.readline


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(blind):
    check = [[False] * n for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if check[i][j] == False:
                ans += 1
                q = deque()
                q.append((i, j))
                check[i][j] = True

                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == False:
                            if pictures[x][y] == pictures[nx][ny]:
                                check[nx][ny] = True
                                q.append((nx, ny))
                            # 적록색약인 경우
                            if blind == True:
                                if (pictures[x][y] == "G" and pictures[nx][ny] == "R") or \
                                        (pictures[x][y] == "R" and pictures[nx][ny] == "G"):
                                    check[nx][ny] = True
                                    q.append((nx, ny))
    return ans

n = int(input())
pictures = [list(input().rstrip()) for _ in range(n)]
print(str(bfs(False)) + " " + str(bfs(True)))