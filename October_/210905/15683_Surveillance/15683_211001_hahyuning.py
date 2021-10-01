from copy import deepcopy

# 2. cctv 방향 결정
def solution(idx, dir):
    if idx == len(cctv):
        b = deepcopy(a)
        for i in range(len(cctv)):
            ctype, x, y = cctv[i]
            if ctype == 1:
                check(b, x, y, dir[i])
            elif ctype == 2:
                check(b, x, y, dir[i])
                check(b, x, y, (dir[i] + 2) % 4)
            elif ctype == 3:
                check(b, x, y, dir[i])
                check(b, x, y, (dir[i] + 1) % 4)
            elif ctype == 4:
                check(b, x, y, dir[i])
                check(b, x, y, (dir[i] + 1) % 4)
                check(b, x, y, (dir[i] + 2) % 4)
            else:
                check(b, x, y, dir[i])
                check(b, x, y, (dir[i] + 1) % 4)
                check(b, x, y, (dir[i] + 2) % 4)
                check(b, x, y, (dir[i] + 3) % 4)

        cnt = 0
        for i in range(n):
            for j in range(m):
                if b[i][j] == 0:
                    cnt += 1
        return cnt

    ans = 100
    for i in range(4):
        tmp = solution(idx + 1, dir + [i])
        ans = min(ans, tmp)
    return ans

# 3. 사각지대 크기 구하기
def check(b, x, y, dir):
    i, j = x, y
    while 0 <= i < n and 0 <= j < m:
        if a[i][j] == 6:
            break
        b[i][j] = a[x][y]
        i += dx[dir]
        j += dy[dir]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

cctv = []
# 1. cctv 위치 찾기
for i in range(n):
    for j in range(m):
        if a[i][j] in [1, 2, 3, 4, 5]:
            cctv.append((a[i][j], i, j))

print(solution(0, []))
