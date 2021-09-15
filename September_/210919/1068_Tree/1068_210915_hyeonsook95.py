import sys

input = sys.stdin.readline

N = int(input().strip())
nodes = list(map(int, input().split()))
target = int(input().strip())

visited = [False for _ in range(N)]
visited[target] = True

start_v = None
tree = [list() for _ in range(N)]
for idx, node in enumerate(nodes):
    if node == -1:
        start_v = idx
    else:
        tree[node].append(idx)


def dfs(start_v):
    if visited[start_v]:
        return 0

    cnt = 0
    visited[start_v] = True
    stack = [start_v]
    while stack:
        v = stack.pop()
        children = 0
        for w in tree[v]:
            if not visited[w]:
                children += 1
                visited[w] = True
                stack.append(w)
        if children == 0:
            cnt += 1
    return cnt


print(dfs(start_v))
