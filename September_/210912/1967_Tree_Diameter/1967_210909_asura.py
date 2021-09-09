import sys
sys.setrecursionlimit(10**9) # 재귀제한 풀기. 안풀면 RecursionError.

def dfs(start,wei):
    for i in tree[start]:
        x,y = i
        if distance[x] == -1:
            distance[x] = wei + y
            dfs(x,wei+y)

N = int(input())
tree = [[] for _ in range(N+1)]

# 트리 구현하기.
for _ in range(N-1):
    a, b, weight = map(int,input().split())
    tree[a].append([b,weight])
    tree[b].append([a,weight])

# 트리에서 가장 먼 노드 찾기. distance 배열 가장 큰 값을 가진 인덱스가 가장 먼 노드
distance = [-1] * (N+1)
distance[1] = 0
dfs(1,0)

# 위에서 찾은 노드에서 가장 먼 노드 찾기
first_node = distance.index(max(distance))
distance = [-1] * (N+1)
distance[first_node] = 0
dfs(first_node,0)

print(max(distance))
