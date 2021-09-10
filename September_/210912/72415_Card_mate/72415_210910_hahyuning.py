import sys
from collections import defaultdict, deque
from itertools import permutations
from copy import deepcopy

def solution(board, r, c):
    numbers = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                numbers[board[i][j]] += [i, j]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(sx, sy, ex, ey):
        q = deque()
        check = [[-1] * 4 for _ in range(4)]
        q.append((sx, sy))
        check[sx][sy] = 0

        while q:
            x, y = q.popleft()
            cost = check[x][y] + 1
            for k in range(4):
                one_cost = cost
                l = 1
                while True:
                    nx, ny = x + dx[k] * l, y + dy[k] * l
                    if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                        nx -= dx[k]
                        ny -= dy[k]
                        if cost < check[nx][ny]:
                            check[nx][ny] = cost
                        break

                    if a[nx][ny] > 0:
                        if check[nx][ny] == -1 or cost < check[nx][ny]:
                            check[nx][ny] = cost
                            q.append((nx, ny))
                        break

                    if check[nx][ny] == -1 or one_cost < check[nx][ny]:
                        check[nx][ny] = one_cost
                        q.append((nx, ny))
                    one_cost += 1
                    l += 1
        return check[ex][ey]


    n = len(numbers.keys()) * 2
    def simulate(sx, sy, idx, cnt, order, path):
        nonlocal ans

        if idx == n:
            ans = min(ans, cnt)
            return

        num = order[idx // 2]
        # 첫 번째 블록을 찾는 경우
        if idx % 2 == 0:
            x1, y1, x2, y2 = numbers[num]
            simulate(x1, y1, idx + 1, cnt + bfs(sx, sy, x1, y1), order, path + [x1, y1])
            simulate(x2, y2, idx + 1, cnt + bfs(sx, sy, x2, y2), order, path + [x2, y2])

        # 두 번재 블록을 찾는 경우
        else:
            x1, y1, x2, y2 = numbers[num]
            if (sx, sy) == (x1, y1):
                d = bfs(x1, y1, x2, y2)
                a[x1][y1] = 0
                a[x2][y2] = 0
                simulate(x2, y2, idx + 1, cnt + d + 2, order, path + [x2, y2])
                a[x1][y1] = num
                a[x2][y2] = num
            else:
                d = bfs(x2, y2, x1, y1)
                a[x1][y1] = 0
                a[x2][y2] = 0
                simulate(x1, y1, idx + 1, cnt + d + 2, order, path + [x1, y1])
                a[x1][y1] = num
                a[x2][y2] = num

    ans = sys.maxsize
    permutation = list(permutations(numbers.keys()))
    for order in permutation:
        sx, sy = r, c
        a = deepcopy(board)
        simulate(sx, sy, 0, 0, order, [sx, sy])

    return ans