n = int(input())
arr = list(map(int, input().split()))
r = int(input())

node = [[] for _ in range(n)]
root = 0
for a in range(n):
    if arr[a] == -1:
        root = a
    elif a != r:
        node[arr[a]].append(a)


def dfs(x):
    if not node[x]:
        return 1
    ans = 0
    for i in node[x]:
        ans += dfs(i)
    return ans


if root == r:
    print(0)
else:
    print(dfs(root))
