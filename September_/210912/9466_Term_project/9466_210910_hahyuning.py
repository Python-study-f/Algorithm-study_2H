import sys
sys.setrecursionlimit(10 ** 5)

def dfs(x):
    global id
    id += 1
    d[x] = id
    stack.append(x)

    parent = d[x]
    for y in graph[x]:
        if d[y] == 0:
            parent = min(parent, dfs(y))
        elif not finished[y]:
            parent = min(parent, d[y])

    if parent == d[x]:
        scc = []
        while True:
            t = stack.pop()
            scc.append(t)
            finished[t] = True
            if t == x:
                break
        SCC.append(scc)

    return parent

t = int(input())
for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    a = list(map(int, input().split()))
    for i, x in enumerate(a, start=1):
        graph[i].append(x)

    d = [0] * (n + 1)
    id = 0
    stack = []
    finished = [False] * (n + 1)
    SCC = []

    for i in range(1, n + 1):
        if d[i] == 0:
            dfs(i)

    ans = n
    for x in SCC:
        if len(x) == 1 and graph[x[0]][0] == x[0]:
            ans -= 1
        elif len(x) > 1:
            ans -= len(x)
    print(ans)