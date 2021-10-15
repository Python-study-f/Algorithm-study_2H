import sys

sys.setrecursionlimit(10 ** 6)

a = int(input())
array = [list(map(int, input().split())) for _ in range(a)]
visit = [[0] * a for i in range(a)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = 0


def dfs(x, y):
    if visit[x][y] != 0:
        return visit[x][y]
    visit[x][y] = 1
    # 4방향 방문
    for d in range(4):
        tx = dx[d] + x
        ty = dy[d] + y
        if 0 <= tx < a and 0 <= ty < a:
            if array[x][y] < array[tx][ty]:
                visit[x][y] = max(visit[x][y], dfs(tx, ty) + 1)
    return visit[x][y]


for x in range(a):
    for y in range(a):
        result = max(result, dfs(x, y))

print(result)
