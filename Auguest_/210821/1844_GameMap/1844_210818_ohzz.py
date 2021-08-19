# 게임 맵 최단거리 1844 프로그래머스

from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    answer = 0
    q = deque()
    q.append([0, 0])

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                q.append([nx, ny])
                maps[nx][ny] = maps[x][y] + 1

    answer = maps[n - 1][m - 1]
    if answer == 1:
        return -1
    return answer


# maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]

# print(solution(maps))
