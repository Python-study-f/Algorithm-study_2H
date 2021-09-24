T = int(input())
dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, -1, 1, 1, -1]
for test_case in range(1, T+1):
    N = int(input())
    mp = [list(input()) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if mp[i][j] == ".":
                num = 0
                for k in range(8):
                    ti, tj = i + dx[k], j + dy[k]
                    if 0 <= ti < N and 0 <= tj < N and mp[ti][tj] == "*":
                        num += 1
                visit[i][j] = num

    def dfs(x, y):
        for d in range(8):
            tx, ty = x + dx[d], y + dy[d]
            if 0 <= tx < N and 0 <= ty < N and mp[tx][ty] == '.':
                mp[tx][ty] = str(visit[tx][ty])
                if visit[tx][ty] == 0:
                    dfs(tx, ty)
    result = 0
    for i in range(N):
        for j in range(N):
            if mp[i][j] == '.' and visit[i][j] == 0:
                mp[i][j] = str(visit[i][j])
                dfs(i, j)
                result += 1
    for i in range(N):
        for j in range(N):
            if mp[i][j] == '.':
                result += 1

    print("#{} {}".format(test_case, result))
