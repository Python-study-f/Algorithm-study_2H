# 아기상어 16236 백준

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

sea = [list(map(int, input().split())) for _ in range(n)]
fish_cnt = 0  # 물고기 수
shark_size = 2  # 상어 크기
shark_eat = 0  # 상어 먹이먹은 횟수
time = 0  # 먹이를 먹는데 걸린 시간 (답)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


for i in range(n):
    for j in range(n):
        if 1 <= sea[i][j] <= 6:
            fish_cnt += 1  # 먹이의 수
        elif sea[i][j] == 9:
            shark_x, shark_y = i, j  # 상어 현재 위치

while fish_cnt:
    q = deque()
    q.append([shark_x, shark_y, 0])
    move_list = []
    sea[shark_x][shark_y] = 0  # 상어 현재 위치 0
    visited = [[0] * n for _ in range(n)]
    visited[shark_x][shark_y] = 1
    move_min = int(1e9)

    while q:
        x, y, cur_move = q.popleft()
        for i in range(4):
            tmp_x = dx[i] + x
            tmp_y = dy[i] + y
            if 0 <= tmp_x < n and 0 <= tmp_y < n and not visited[tmp_x][tmp_y]:
                if sea[tmp_x][tmp_y] <= shark_size:
                    visited[tmp_x][tmp_y] = 1

                    # 물고기를 먹을 때
                    if 0 < sea[tmp_x][tmp_y] < shark_size:
                        move_min = cur_move
                        move_list.append([cur_move + 1, tmp_x, tmp_y])
                    if cur_move + 1 <= move_min:
                        q.append([tmp_x, tmp_y, cur_move + 1])
    if move_list:
        move_list.sort()
    else:
        break
    res = move_list[0]
    shark_x, shark_y = res[1], res[2]
    time += res[0]
    shark_eat += 1
    fish_cnt -= 1
    if shark_size == shark_eat:
        shark_eat = 0
        shark_size += 1

print(time)
