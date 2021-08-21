for T in range(1, 11):
    N = int(input())
    mp = [list(map(int, input().split())) for _ in range(N)]
    
    # 각 S극, N극으로 떨어질 자석 정리
    for j in range(N):
        for i in range(N):
            if mp[i][j] == 1:
                break
            elif mp[i][j] == 2:
                mp[i][j] = 0
        for i in range(N - 1, -1, -1):
            if mp[i][j] == 2:
                break
            elif mp[i][j] == 1:
                mp[i][j] = 0

    # 교착 상태 자석 갯수 세기 - S/N극의 쌍 갯수만 세면 됨
    answer = 0
    for j in range(N):
        mag = 0
        for i in range(N):
            if mp[i][j] != 0:
                if mp[i][j] != mag and mp[i][j] ==2:
                    answer += 1
                mag = mp[i][j]

    print("#{} {}".format(T, answer))
