import sys

input = sys.stdin.readline


import collections


def solution(N, M, G):
    m = []
    graph = collections.defaultdict(list)
    goals = collections.defaultdict(tuple)
    for _ in range(N):
        m.append(list(map(int, input().split())))

    taxi_r, taxi_c = map(lambda x: int(x) - 1, input().split())

    for _ in range(M):
        s_r, s_c, g_r, g_c = map(lambda x: int(x) - 1, input().split())

        m[s_r][s_c] = 2
        goals[(s_r, s_c)] = (g_r, g_c)

    for r in range(N):
        for c in range(N):
            # graph
            if m[r][c] == 1:
                continue
            if r > 0 and m[r - 1][c] != 1:
                graph[(r, c)].append((r - 1, c))
            if c > 0 and m[r][c - 1] != 1:
                graph[(r, c)].append((r, c - 1))
            if c < N - 1 and m[r][c + 1] != 1:
                graph[(r, c)].append((r, c + 1))
            if r < N - 1 and m[r + 1][c] != 1:
                graph[(r, c)].append((r + 1, c))

    def find_customers(t_r, t_c, gas):
        visited = [[-1 for _ in range(N)] for _ in range(N)]
        queue = collections.deque([(t_r, t_c)])
        visited[t_r][t_c] = 0
        customers = []

        if m[t_r][t_c] == 2:
            customers.append((0, t_r, t_c))

        while queue:
            v = queue.popleft()
            for r, c in graph[v]:
                if visited[r][c] == -1:
                    visited[r][c] = visited[v[0]][v[1]] + 1
                    queue.append((r, c))
                    if m[r][c] == 2 and visited[r][c] <= gas:
                        customers.append((visited[r][c], r, c))
        return customers

    def to_goal(t_r, t_c, gas):
        visited = [[-1 for _ in range(N)] for _ in range(N)]
        queue = collections.deque([(t_r, t_c)])
        visited[t_r][t_c] = 0

        while queue:
            v = queue.popleft()
            for r, c in graph[v]:
                if visited[r][c] == -1:
                    visited[r][c] = visited[v[0]][v[1]] + 1
                    queue.append((r, c))
                    if visited[r][c] > gas:
                        return -1, r, c
                    if goals[(t_r, t_c)] == (r, c):
                        return (visited[r][c], r, c)
        return -1, t_r, t_c

    gas = G
    customers = [(taxi_r, taxi_c)]
    while customers:

        customers = find_customers(taxi_r, taxi_c, gas)

        if customers:
            u_g, c_r, c_c = sorted(customers)[0]

            m[c_r][c_c] = 0
            gas = gas - u_g

            u_g, taxi_r, taxi_c = to_goal(c_r, c_c, gas)

            gas = gas + u_g
            M -= 1

            if u_g < 0:
                customers = []
    if M != 0:
        return -1

    return gas


N, M, G = map(int, input().split())
print(solution(N, M, G))
