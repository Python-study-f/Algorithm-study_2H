from itertools import combinations
from copy import deepcopy

def find_dist(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

# 2. 궁수 공격
def attack(archer, enemy):
    global attack_cnt

    k = len(enemy.keys())
    dist = [[0] * k for _ in range(3)]
    for i, x in enumerate(archer):
        for j, y in enumerate(enemy.values()):
            dist[i][j] = find_dist(x, y)

    tmp = [-1] * 3
    for i in range(3):
        min_dist = d + 1
        min_idx = -1
        for j in range(k):
            if dist[i][j] <= d and dist[i][j] <= min_dist:
                min_dist = dist[i][j]
                min_idx = j
        tmp[i] = min_idx

    for x in tmp:
        if x in enemy.keys():
            attack_cnt += 1
            board[enemy[x][0]][enemy[x][1]] = 0
            del enemy[x]
    return enemy

n, m, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 1. 궁수 배치
c = combinations([i for i in range(m)], 3)
ans = -1
for x in c:
    board = deepcopy(a)
    enemy = dict()
    cnt = -1
    for j in range(m - 1, -1, -1):
        for i in range(n - 1, -1, -1):
            if board[i][j] == 1:
                cnt += 1
                enemy[cnt] = (i, j)

    archer = []
    for i in x:
        archer.append((n, i))

    attack_cnt = 0
    while True:
        enemy = attack(archer, enemy)

        # 3. 적 전진
        new = dict()
        cnt = -1
        for i, x in enemy.items():
            if x[0] + 1 == n:
                board[x[0]][x[1]] = 0
            else:
                board[x[0]][x[1]] = 0
                board[x[0] + 1][x[1]] = 1
                cnt += 1
                new[cnt] = (x[0] + 1, x[1])

        # 4. 남아있는 적 확인
        if len(new.keys()) == 0:
            break
        enemy = new

    ans = max(attack_cnt, ans)

print(ans)
