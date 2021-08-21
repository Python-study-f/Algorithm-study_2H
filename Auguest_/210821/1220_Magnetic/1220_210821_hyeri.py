for T in range(1, 11):
    N = int(input())
    mp = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for j in range(N):
        mag = 0
        for i in range(N):
            if mp[i][j] != 0:
                if mp[i][j] == 2 and mag == 1:
                    answer += 1
                mag = mp[i][j]


    print("#{} {}".format(T, answer))
