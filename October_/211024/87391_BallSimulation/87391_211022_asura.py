def solution(n, m, x, y, queries):
    left, right, up, down = y, y, x, x
    queries.reverse()

    for query in queries:
        d, length = query

        if d == 0:  # 왼쪽
            if left == 0:
                right = min(m - 1, right + length)
            else:
                left += length
                right = min(m - 1, right + length)

        elif d == 1:  # 오른쪽
            if right == m - 1:
                left = max(0, left - length)
            else:
                left = max(0, left - length)
                right = right - length
        elif d == 2:
            if up == 0:
                down = min(n - 1, down + length)
            else:
                down = min(n - 1, down + length)
                up = up + length
        else:  # d가 3일때
            if down == n - 1:
                up = max(0, up - length)
            else:
                up = max(0, up - length)
                down = down - length

        if left > right:  # 테케 33번
            return 0

    ret = (down - up + 1) * (right - left + 1)
    return ret