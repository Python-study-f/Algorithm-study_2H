from collections import deque

for _ in range(10):
    t, m = map(int, input().split())
    graph = [[] for _ in range(100)]

    a = list(map(int, input().split()))
    for i in range(0, len(a), 2):
        s, e = a[i], a[i + 1]
        graph[s].append(e)

    q = deque()
    q.append(0)

    while q:
        now = q.popleft()
        if now == 99:
            print("#{}".format(t), 1)
            break
        for nxt in graph[now]:
            q.append(nxt)
    else:
        print("#{}".format(t), 0)