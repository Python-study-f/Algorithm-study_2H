from collections import deque

def bfs(arr, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dist = [[-1] * 5 for _ in range(5)]
    q = deque()
    q.append((x, y))
    dist[x][y] = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < 5 and 0 <= ny < 5 and dist[nx][ny] == -1:
                if arr[nx][ny] == "P" or arr[nx][ny] == "O":
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

                    if arr[nx][ny] == "P" and dist[nx][ny] <= 2:
                        return False
    return True


def solution(places):
    answer = []

    for case in places:
        check = False
        for i in range(5):
            for j in range(5):
                if case[i][j] == "P":
                    if not bfs(case, i, j):
                        answer.append(0)
                        check = True
                        break
            if check:
                break
        else:
            answer.append(1)
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))