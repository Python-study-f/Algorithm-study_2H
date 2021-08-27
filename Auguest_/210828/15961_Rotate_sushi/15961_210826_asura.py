# 풀이 - Two point
import sys
from collections import defaultdict

N, d, k, c = map(int, sys.stdin.readline().split())

sushi = [int(sys.stdin.readline()) for _ in range(N)]
sushi.extend(sushi)  # 원형 queue로 생성 / 다들 원형 큐 유형의 문제 나오면 어떻게 연결시키시나요?

kind_count = 0
start, end = 0, 0
eat = defaultdict(int)  # int형 dictionary 생성

eat[c] += 1  # 이거 왜 넣어줘야 하나요? 이거 조건때문에 계속 시간초과 뜨더라고요..

for end in range(len(sushi)):
    eat[sushi[end]] += 1

    if end >= k - 1:
        kind_count = max(kind_count, len(eat))
        eat[sushi[start]] -= 1

        if eat[sushi[start]] == 0:
            del eat[sushi[start]]
        start += 1

print(kind_count)
