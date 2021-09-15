from collections import deque, defaultdict

n = int(input())
parent = list(map(int, input().split()))
delete = int(input())
tree = defaultdict(list)

for i in range(n):
    if i != delete and parent[i] != delete:
        tree[parent[i]].append(i)

q = deque()
if -1 in tree:
    q.append(-1)

ans = 0
while q:
    now = q.popleft()
    if not tree[now]:
        ans += 1
        continue

    for nxt in tree[now]:
        q.append(nxt)

print(ans)