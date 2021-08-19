from collections import deque, defaultdict

n, l = map(int, input().split())
graph = defaultdict(list)
subway = [[]]
for k in range(1, l + 1):
    num = list(map(int, input().split()))
    subway.append(num[:-1])

    for x in num[:-1]:
        graph[x].append(-k)
        graph[-k].append(x)

s, e = map(int, input().split())
dist = defaultdict(int)
q = deque()
for i in range(1, l + 1):
    if s in subway[i]:
        q.append(-i)

while q:
    now = q.popleft()

    for nxt in graph[now]:
        if nxt not in dist:
            if nxt < 0:
                dist[nxt] = dist[now] + 1
            else:
                dist[nxt] = dist[now]
            q.append(nxt)

if e in dist:
    print(dist[e])
else:
    print(-1)
