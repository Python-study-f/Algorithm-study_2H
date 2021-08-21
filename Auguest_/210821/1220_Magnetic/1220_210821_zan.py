for T in range(1, 11):
    N = int(input().strip())
    m = [list(map(int, input().split())) for _ in range(N)]

    dead_lock = [False for _ in range(N)]
    cnt = 0

    for r in range(N):
        for c in range(N):
            if m[r][c] == 1 and not dead_lock[c]:
                dead_lock[c] = True
            elif m[r][c] == 2 and dead_lock[c]:
                dead_lock[c] = False
                cnt += 1

    print(f"#{T} {cnt}")
