from itertools import combinations
from collections import deque

def bfs(group, start):
    check = [False] * (n + 1)
    q = deque()
    q.append(start)
    check[start] = True

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if not check[nxt] and nxt in group:
                check[nxt] = True
                q.append(nxt)
    return check

n = int(input())
people = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    m, *a = map(int, input().split())
    for x in a:
        graph[i].append(x)

cities = [i for i in range(1, n + 1)]
total = sum(people)
ans = -1
for i in range(1, n // 2 + 1):
    all_combi = combinations(cities, i)

    for group1 in all_combi:
        flag = False
        group2 = []
        for x in range(1, n + 1):
            if x not in group1:
                group2.append(x)

        res1 = bfs(group1, group1[0])
        res2 = bfs(group1, group1[0])

        cnt1 = 0
        for x in group1:
            if not res1[x]:
                flag = True
                break
            cnt1 += people[x]

        cnt2 = 0
        for x in group2:
            if not res2[x]:
                flag = True
                break
            cnt2 += people[x]

        if not flag:
            if ans == -1 or abs(cnt1 - cnt2) < ans:
                ans = abs(cnt1 - cnt2)

print(ans)

