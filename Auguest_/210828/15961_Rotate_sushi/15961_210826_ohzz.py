# 회전초밥 15961 백준
import sys
from collections import deque

n, d, k, c = map(int, input().split())
sushirotate = []

for _ in range(n):
    sushirotate.append(int(input()))
sushirotate += sushirotate[: k - 1]

sushilist = [0] * (d + 1)

eatkind = deque()
kindcnt = 0
res = 0

for i, v in enumerate(sushirotate):
    eatkind.append(v)
    sushilist[v] += 1
    if sushilist[v] == 1:
        kindcnt += 1

    if i < k - 1:
        continue

    if sushilist[c] == 0:
        res = max(res, kindcnt + 1)
    else:
        res = max(res, kindcnt)

    e = eatkind.popleft()
    sushilist[e] -= 1
    if sushilist[e] == 0:
        kindcnt -= 1

print(res)
