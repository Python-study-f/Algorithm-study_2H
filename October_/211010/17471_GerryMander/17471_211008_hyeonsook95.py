# 32788kb 108ms
from itertools import combinations
from collections import deque


def solution(N):
    nodes = list(map(int, input().strip().split()))
    graph = [
        list(map(lambda x: int(x) - 1, input().strip().split()))[1:] for _ in range(N)
    ]

    total = sum(nodes)

    def bfs(group):
        visited = [False] * N
        visited[group[0]] = True
        queue = deque([group[0]])
        while queue:
            v = queue.popleft()
            for w in graph[v]:
                if not visited[w] and w in group:
                    queue.append(w)
                    visited[w] = True
        return sum(visited) == len(group)

    ans = int(1e9)
    for n in range(1, int(N / 2 + 0.5) + 1):
        for A in combinations(range(N), n):
            dist = abs(total - (sum([nodes[idx] for idx in A]) * 2))
            if ans > dist:
                B = set(range(N)) - set(A)
                if bfs(list(A)) and bfs(list(B)):
                    ans = dist
    if ans == int(1e9):
        return -1
    return ans


if __name__ == "__main__":
    print(solution(int(input().strip())))
