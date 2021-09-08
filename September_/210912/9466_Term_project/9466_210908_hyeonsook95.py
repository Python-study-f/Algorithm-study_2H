import sys, collections

input = sys.stdin.readline

T = int(input().strip())


for _ in range(T):
    N = int(input().strip())
    visited = [True] + [False] * N
    students = [0] + list(map(int, input().split()))

    def dfs(start_v):
        if start_v == students[start_v]:
            visited[start_v] = True
            return 1

        trace = [start_v]
        visited[start_v] = True
        q = collections.deque([start_v])
        while q:
            v = q.popleft()
            w = students[v]
            if visited[w]:
                if w in trace:
                    return len(trace[trace.index(w) :])
                return 0
            else:
                visited[w] = True
                trace.append(w)
                q.append(w)
        return 0

    cnt = 0
    for s in range(1, N + 1):
        if not visited[s]:
            cnt += dfs(s)

    print(N - cnt)
