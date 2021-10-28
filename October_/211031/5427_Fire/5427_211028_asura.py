from collections import deque
import sys

input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    pq.append((x,y))
    visited[x][y] = 1

    while pq:
        exeCount = len(pq)
        while exeCount:
            x, y = pq.popleft()
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]

                if 0 <= nx < h and 0 <= ny < w:
                    if lst[nx][ny] == '.' and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        pq.append([nx, ny])
                else:
                    print(visited[x][y])
                    return
            exeCount -= 1
        fire()

    print("IMPOSSIBLE")
    return


def fire():
    exeCount = len(fq)

    while exeCount: # 정해진 카운트로만 하기
        x, y = fq.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < h and 0 <= ny < w:
                if lst[nx][ny] == '.':
                    lst[nx][ny] = '*'
                    fq.append((nx,ny))
        exeCount -= 1
    #함수가 종료되도 그대로 데이터가 남아 있음. 따로 배열 만들 필요 없으니깐 까먹지 말자.


T = int(input())
for tc in range(T):
    w, h = map(int, input().split())
    lst = [list(map(str, input().strip())) for _ in range(h)]
    fq, pq = deque(), deque() # fireQueue, peopleQueue
    visited = [[0] * w for _ in range(h)]
    sx,sy = -1, -1

    for i in range(h):
        for j in range(w):
            if lst[i][j] == '@':
                sx,sy = i,j
                lst[i][j] = '.'
            elif lst[i][j] == '*':
                fq.append([i, j])
    fire()
    bfs(sx, sy)
