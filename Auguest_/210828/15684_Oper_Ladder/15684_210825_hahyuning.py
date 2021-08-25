# 2. 체크
def check():
    for i in range(n):
        col = i
        for row in range(h):
            if lines[row][col] == 1:
                col += 1
            elif lines[row][col] == 2:
                col -= 1

        if col != i:
            return False
    return True


# 1. 가로선 넣기
def recursion(cnt, idx):
    global ans

    if check():
        if ans == -1 or cnt < ans:
            ans = cnt
        return

    if cnt >= 3 or idx >= n * h - 1:
        return

    x = idx // n
    y = idx % n

    # 가로선을 넣을 수 있는 경우
    if y + 1 < n and lines[x][y] == 0 and lines[x][y + 1] == 0:
        lines[x][y] = 1
        lines[x][y + 1] = 2
        recursion(cnt + 1, idx + 1)
        lines[x][y] = 0
        lines[x][y + 1] = 0

    # 가로선을 안 넣는 경우
    recursion(cnt, idx + 1)


n, m, h = map(int, input().split())
lines = [[0] * n for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    lines[a][b] = 1
    lines[a][b + 1] = 2

ans = -1
recursion(0, 0)
print(ans)