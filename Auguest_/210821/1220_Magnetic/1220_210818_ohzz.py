# Magnetic 1220 SW expert

for T in range(1, 11):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    for y in range(n):
        deadlock_check = False
        for x in range(n):
            if table[x][y] == 1 and not deadlock_check:
                deadlock_check = True
            elif table[x][y] == 2 and deadlock_check:
                deadlock_check = False
                res += 1

    print(f"#{T} {res}")
