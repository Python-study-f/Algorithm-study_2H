t = int(input())
for tc in range(1, t + 1):
    price = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))

    # d[i][j]: i번째 달을 j 방법으로 계산했을 때의 최솟값
    # j가 0이면 1일권, 1이면 1달권, 2면 3달권
    d = [[0 for _ in range(3)] for _ in range(13)]
    for i in range(13):
        d[i][2] = 3000 * 12 + 1

    for i in range(1, 13):
        d[i][0] = min(d[i - 1]) + plan[i] * price[0]

        if plan[i] > 0:
            d[i][1] = min(d[i - 1]) + price[1]
            if i - 3 >= 0:
                d[i][2] = min(d[i - 3]) + price[2]
        else:
            d[i][1] = min(d[i - 1])

    print("#{} {}".format(tc, min(price[3], min(d[12]))))