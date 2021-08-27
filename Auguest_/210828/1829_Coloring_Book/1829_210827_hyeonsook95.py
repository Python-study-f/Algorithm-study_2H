import collections


def solution(m, n, picture):
    area, color_cnt = 0, 0
    pic = [[0 for _ in range(n)] for _ in range(m)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    def bfs(r, c, color):
        cnt = 1
        pic[r][c] = color
        queue = collections.deque([(r, c)])

        while queue:
            vr, vc = queue.popleft()
            for mr, mc in zip(dr, dc):
                wr, wc = vr + mr, vc + mc
                if (
                    0 <= wr < m
                    and 0 <= wc < n
                    and picture[wr][wc] == color
                    and pic[wr][wc] == 0
                ):
                    cnt += 1
                    pic[wr][wc] = color
                    queue.append((wr, wc))
        return cnt

    for r in range(m):
        for c in range(n):
            if picture[r][c] > 0 and pic[r][c] == 0:
                color_cnt = max(color_cnt, picture[r][c])
                area = max(area, bfs(r, c, picture[r][c]))

    return [color_cnt + 1, area]


m, n = 6, 4
picture = [
    [1, 1, 1, 0],
    [1, 2, 2, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 3],
    [0, 0, 0, 3],
]
print(solution(m, n, picture))
