# 개똥벌레 3090 백준

bottom = []
top = []

n, h = map(int, input().split())

for i in range(n):
    k = int(input())
    if i % 2 == 0:
        bottom.append(k)
    else:
        top.append(k)


def checkStone(h, arr):
    lt, rt = 0, len(arr) - 1
    while lt <= rt:
        mid = (lt + rt) // 2
        if arr[mid] <= h:
            lt = mid + 1
        else:
            rt = mid - 1
    return len(arr) - (rt + 1)


bottom.sort()
top.sort()

ans = 21474836
cnt = 0

for i in range(1, 1 + h):
    bottom_cnt = checkStone(i - 1, bottom)
    top_cnt = checkStone(h - i, top)
    total_cnt = bottom_cnt + top_cnt

    if total_cnt < ans:
        cnt = 1
        ans = total_cnt
    elif total_cnt == ans:
        cnt += 1

print(ans, cnt)
