for _ in range(1):
    TC = int(input())
    matrix1 = []
    for _ in range(100):
        matrix1.append(input().strip())
    matrix2 = list(map(list, list(zip(*matrix1))))

    L = 0
    for n in range(100):
        row = matrix1[n]
        column = matrix2[n]
        for i in range(100):
            for j in range(i + 1, 101):
                # 행 검사
                if row[i:j] == row[i:j][::-1]:
                    L = max(L, len(row[i:j]))

                # 열 검사
                if column[i:j] == column[i:j][::-1]:
                    L = max(L, len(column[i:j]))
    print(f"{TC} {L}")
