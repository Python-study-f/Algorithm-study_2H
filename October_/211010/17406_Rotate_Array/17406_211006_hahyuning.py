from copy import deepcopy


# 1. 회전 순서 정하기
def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[j] <= a[i - 1]:
        j -= 1

    a[i - 1], a[j] = a[j], a[i - 1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True


# 2. 회전 연산
def rotate(a, info):
    row, col, size = info
    groups = []
    # 그룹 나누기
    for s in range(1, size + 1):
        group = []
        # (r-s, c-s) -> (r-s, c+s)
        for c in range(col - s, col + s):
            group.append(a[row - s][c])
        # (r-s, c+s) -> (r+s, c+s)
        for r in range(row - s, row + s):
            group.append(a[r][col + s])
        # (r+s, c+s) -> (r+s, c-s)
        for c in range(col + s, col - s, -1):
            group.append(a[row + s][c])
        # (r+s, c-s) -> (r-s, c-s)
        for r in range(row + s, row - s, -1):
            group.append(a[r][col - s])
        groups.append(group)

    # 각 그룹별로 회전
    for s in range(1, size + 1):
        group = groups[s - 1]
        group = group[-1:] + group[:-1]
        index = 0
        # (r-s, c-s) -> (r-s, c+s)
        for c in range(col - s, col + s):
            a[row - s][c] = group[index]
            index += 1
        # (r-s, c+s) -> (r+s, c+s)
        for r in range(row - s, row + s):
            a[r][col + s] = group[index]
            index += 1
        # (r+s, c+s) -> (r+s, c-s)
        for c in range(col + s, col - s, -1):
            a[row + s][c] = group[index]
            index += 1
        # (r+s, c-s) -> (r-s, c-s)
        for r in range(row + s, row - s, -1):
            a[r][col - s] = group[index]
            index += 1


n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

rotation = []
for _ in range(k):
    r, c, s = map(int, input().split())
    rotation.append((r - 1, c - 1, s))
rotation.sort()

ans = 10000
while True:
    b = deepcopy(a)
    for info in rotation:
        rotate(b, info)

    # 3. 최솟값 구하기
    for i in range(n):
        tmp = sum(b[i])
        if tmp < ans:
            ans = tmp

    if not next_permutation(rotation):
        break
print(ans)