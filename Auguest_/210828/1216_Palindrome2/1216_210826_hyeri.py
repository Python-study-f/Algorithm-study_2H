for test_case in range(1, 11):
    T = int(input())
    mp = [list(input()) for _ in range(100)]
    result = 0

    # brute-force
    def check(x, y, e, row):
        if row:
            for ty in range(int((e - y) / 2)+1):
                if mp[x][y + ty] != mp[x][e - ty]:
                    return -1
            else:
                return e - y + 1
        else:
            for tx in range(int((e - x) / 2)+1):
                if mp[x + tx][y] != mp[e - tx][y]:
                    return -1
            else:
                return e - x + 1


    for i in range(100):
        for j in range(100):
            for k in range(j + 1, 100):
                result = max(result, check(i, j, k, True))
            for k in range(i + 1, 100):
                result = max(result, check(i, j, k, False))

    print("#{} {}".format(T, result))
