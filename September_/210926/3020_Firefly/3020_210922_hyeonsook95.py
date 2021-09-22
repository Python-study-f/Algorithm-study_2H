import sys
from collections import Counter

"""
# 시간초과
input = sys.stdin.readline

N, H = map(int, input().split())
cave = [0] * H
for n in range(N):
    block = int(input().strip())
    if n % 2 == 0:
        start = 0
        end = block
    else:
        start = H - block
        end = H

    for idx in range(start, end):
        cave[idx] += 1

cave = Counter(cave)
key = sorted(cave)[0]

print(key, cave[key])
"""

# https://hongcoding.tistory.com/6
input = sys.stdin.readline
N, H = map(int, input().split())

top = [0] * (H + 1)  # 종유석
bottom = [0] * (H + 1)  # 석순

# 입력
for n in range(N):
    num = int(input().strip())
    if n % 2:
        top[num] += 1
    else:
        bottom[num] += 1

# 누적합
for h in range(H - 1, 0, -1):
    top[h] += top[h + 1]
    bottom[h] += bottom[h + 1]

distroyed = N + 1
stalacties = [0] * (H + 1)
for h in range(1, H + 1):
    stalacties[h] = top[H - h + 1] + bottom[h]
    distroyed = min(distroyed, stalacties[h])

print(distroyed, Counter(stalacties[1:])[distroyed])
