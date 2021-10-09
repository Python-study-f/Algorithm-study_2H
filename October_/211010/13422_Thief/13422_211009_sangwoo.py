import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    result = 0
    n, m, k = map(int, sys.stdin.readline().split())
    array = list(map(int, sys.stdin.readline().split()))
    if m == n and sum(array) < k:
        result = 1
    else:
        q = deque()
        right, total = 0, 0
        for left in range(n):
            while len(q) < m and right < n + m - 1:
                q.append(array[right%n])
                total += array[right%n]
                right += 1
            if total < k:
                result += 1
            total -= q.popleft()
    print(result)
