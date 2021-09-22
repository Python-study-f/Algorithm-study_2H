from bisect import bisect_left
from collections import Counter
import sys
input = sys.stdin.readline


n, h = map(int, input().split())
a = []
b = []

for i in range(n):
    x = int(input())
    if i % 2 == 0:
        a.append(x)
    else:
        b.append(h - x)

a.sort()
b.sort()

ans = []
cnt = n
for i in range(1, h + 1):
    x = bisect_left(a, i)
    y = bisect_left(b, i)

    tmp = n // 2 - x + y
    if tmp <= cnt:
        cnt = tmp
        ans.append(cnt)

ans.sort()
c = Counter(ans)
tmp = list(c.keys())

print(tmp[0], c[tmp[0]])