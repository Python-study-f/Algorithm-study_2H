# 거리두기 확인하기 81302 프로그래머스

from collections import deque


def solution(places):
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    ans = []

    def bfs(px, py):
        q = deque()
        q.append([px, py, 0])
        visited = [[False] * 5 for _ in range(5)]

        while q:
            x, y, d = q.popleft()
            visited[x][y] = True

            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == False:
                    if place[nx][ny] == "P":
                        if d < 2:
                            return False
                    if place[nx][ny] == "O" or place[nx][ny] == "P":
                        q.append([nx, ny, d + 1])
        return True

    cnt = 0
    for place in places:
        candidates = []

        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    candidates.append([i, j])

        res = 1
        cnt += 1
        for px, py in candidates:
            if not bfs(px, py):
                res = 0
                break
        ans.append(res)

    return ans


places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
]

print(solution(places))
