n = int(input())
k = int(input())

if k == 1:
    print(n % 1000000003)
else:
    # d[i][j]: i 개의 색이 있다고 할 때, 그 중 j 개의 색을 고르는 경우의 수
    d = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        d[i][1] = i
        d[i][0] = 1

    for i in range(2, n + 1):
        for j in range(2, k + 1):
            if i != n:
                # Combinatorial proof
                # i 번째 색을 고르지 않는 경우 -> i 번째를 제외한 i - 1 개의 색에서 j 개의 색을 고름
                # i 번째 색을 고르는 경우 -> i, i - 1 번째를 제외한 i - 2 개의 색에서 j - 1 개의 색을 고름
                d[i][j] = (d[i - 1][j] + d[i - 2][j - 1]) % 1000000003
            else:
                # n 번째를 고르지 않는 경우는 똑같이 처리
                # n 번째를 고르는 경우는 1 번째도 고르지 못하므로
                # n - 1, n, 0 번째를 제외한 i - 3 개의 섹에서 j - 1 개의 색을 고름
                d[i][j] = (d[i - 1][j] + d[i - 3][j - 1]) % 1000000003

    print(d[n][k])