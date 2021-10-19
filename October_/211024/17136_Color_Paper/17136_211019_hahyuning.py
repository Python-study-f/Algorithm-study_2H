def solution(num):
    if num == 100:
        for i in range(10):
            for j in range(10):
                if a[i][j] == 1:
                    return -1
        return 0

    x = num // 10
    y = num % 10
    if a[x][y] == 0:
        return solution(num + 1)

    ans = -1
    for k in range(1, 6):
        if cnt[k] > 0:
            # 색종이를 붙일 수 있는지 범위 검사
            if x + k - 1 < 10 and y + k - 1 < 10:
                check = False
                for i in range(x, x + k):
                    for j in range(y, y + k):
                        if a[i][j] == 0:
                            check = True
                            break
                    if check:
                        break
                else:
                    for i in range(x, x + k):
                        for j in range(y, y + k):
                            a[i][j] = 0

                    cnt[k] -= 1
                    tmp = solution(num + 1)

                    if tmp != -1:
                        if ans == -1 or tmp + 1 < ans:
                            ans = tmp + 1

                    cnt[k] += 1
                    for i in range(x, x + k):
                        for j in range(y, y + k):
                            a[i][j] = 1

    return ans

a = [list(map(int, input().split())) for _ in range(10)]
cnt = [0, 5, 5, 5, 5, 5]
print(solution(0))
