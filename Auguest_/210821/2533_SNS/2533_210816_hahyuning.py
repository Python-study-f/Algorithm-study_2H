import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(now):
    d[now][0] = 0
    d[now][1] = 1
    visited[now] = True

    for nxt in tree[now]:
        if not visited[nxt]:
            dfs(nxt)
            d[now][0] += d[nxt][1]
            d[now][1] += min(d[nxt][0], d[nxt][1])

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# d[i][0]: i 번째가 얼리어답터가 아닐때, 얼리어답터의 수
# d[i][1]: i 번째가 얼리어답터일때, 얼리어답터의 수
d = [[0] * 2 for _ in range(n + 1)]
visited = [False] * (n + 1)

dfs(1)
print(min(d[1][0], d[1][1]))