# 와 너무 어렵당...
# 블로그 참조 : https://jjangsungwon.tistory.com/74

import sys
sys.setrecursionlimit(10 ** 9)

def check(array, row, col, depth):  # depth 크기의 색종이를 row, col 위치를 시작점으로 둘 수 있는지 확인
    # 범위 체크
    if row + depth > 10 or col + depth > 10:
        return False
    for i in range(row, row + depth):
        for j in range(col, col + depth):
            if array[i][j] == 0:
                return False
    return True

def dfs(array, remain_cnt, count):
    global result
    if result != -1 and sum(count) > result:
        return

    if remain_cnt == 0:  # 모든 1을 제거한 경우
        if result == -1:
            result = sum(count)
        else:
            result = min(result, sum(count))
        return

    # 이 부분이 핵심
    row, col = -1, -1
    for i in range(10):
        for j in range(10):
            if array[i][j] == 1:
                row, col = i, j
                break
        if (row != -1 and col != -1) and array[row][col] == 1:
            break

    # row, col 위치에 대입 가능한 색종이 탐색
    for i in range(1, 6):
        if count[i - 1] == 5:  # 5개 이상 사용 불가능
            continue
        if check(array, row, col, i):  # 색종이 놓을 수 있는지 확인
            location = []
            for m in range(row, row + i):
                for n in range(col, col + i):
                    array[m][n] = 0
                    location.append((m, n))
            count[i - 1] += 1
            dfs(array, remain_cnt - i ** 2, count)
            count[i - 1] -= 1
            for x, y in location:  # 다시 1로 수정
                array[x][y] = 1


maps = [list(map(int, input().split())) for _ in range(10)]

# 1의 개수 파악
one_num = 0
for i in range(10):
    one_num += maps[i].count(1)

result = -1

# 맵, 1숫자, 색종이를 카운트 할 배열
dfs(maps, one_num, [0, 0, 0, 0, 0])
print(result)