t = int(input())
for i in range(1, t + 1):
    n = int(input())
    ans = [[0] * n for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # 회전 방향 변화
    dir = 0
    # 한 방향에서 진행: n -> n - 1 (x2) -> ... -> 2 (x2) -> 1
    move_cnt = n
    rotation_cnt = 1
    now = 1
    x, y = 0, -1
    while now <= n ** 2:
        for _ in range(move_cnt):
            x += dx[dir]
            y += dy[dir]
            ans[x][y] = now
            now += 1
            if now > n ** 2:
                break

        rotation_cnt += 1
        dir = (dir + 1) % 4
        if rotation_cnt == 2:
            move_cnt -= 1
            rotation_cnt = 0

    print("#{}".format(i))
    for row in ans:
        print(*row)