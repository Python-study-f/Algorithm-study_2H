for t in range(1, 11):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    for j in range(n):

        n_check = False
        for i in range(n):
            if a[i][j] == 1:
                n_check = True
            elif a[i][j] == 2:
                if n_check:
                    cnt += 1
                    n_check = False
    print("#{}".format(t), end=" ")
    print(cnt)

