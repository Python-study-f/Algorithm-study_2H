for _ in range(1):
    T, E = map(int, input().split())
    V = list(map(int, input().split()))

    left = [-1 for _ in range(100)]
    right = [-1 for _ in range(100)]
    for i in range(0, len(V), 2):
        s, e = V[i], V[i + 1]

        if left[s] == -1:
            left[s] = e
        elif right[s] == -1:
            right[s] = e

    def dfs(start_v):
        visited = [False for _ in range(100)]
        stack = [start_v]

        while stack:
            v = stack.pop()
            if not visited[v]:
                visited[v] = True
                if v == 99:
                    return 1
                if left[v] != -1:
                    stack.append(left[v])
                if right[v] != -1:
                    stack.append(right[v])
        return 0

    print(f"#{T} {dfs(0)}")
