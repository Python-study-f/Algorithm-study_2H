def solution(n, s, a, b, fares):
    dist = [[1e9] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    for i, j, cost in fares:
        dist[i][j] = cost
        dist[j][i] = cost

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

    ans = dist[s][a] + dist[a][b]
    for k in range(1, n + 1):
        ans = min(ans, dist[s][k] + dist[k][a] + dist[k][b])

    return ans