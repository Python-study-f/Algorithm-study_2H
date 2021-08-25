# [영역의 개수, 가장 큰 영역의 넓이] 리턴
def solution(m, n, picture):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y, num):
        nonlocal cnt
        check[x][y] = True
        cnt += 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and not check[nx][ny]:
                if picture[nx][ny] == num:
                    dfs(nx, ny, num)

    check = [[False] * n for _ in range(m)]
    ans = 0
    width = 0
    for i in range(m):
        for j in range(n):
            if picture[i][j] != 0 and not check[i][j]:
                ans += 1
                cnt = 0
                dfs(i, j, picture[i][j])
                width = max(width, cnt)

    return [ans, width]