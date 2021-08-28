import sys
from collections import defaultdict
input=sys.stdin.readline
n, d, k, c = map(int, input().split())
data = [int(input()) for _ in range(n)]
dic = defaultdict(int)
dic[c] = 1
cnt = 1
for i in range(k):
    if dic[data[i]] == 0 :
        cnt += 1
    dic[data[i]] += 1
result = cnt
for start in range(n):
    end = (start+k)%n
    dic[data[start]] -= 1
    if dic[data[start]] == 0 :
        cnt -= 1
    if dic[data[end]] == 0:
        cnt += 1
    dic[data[end]] += 1

    result = max(result, cnt)
print(result)