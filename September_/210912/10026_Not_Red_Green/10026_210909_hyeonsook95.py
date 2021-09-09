import sys
import collections

input = sys.stdin.readline


def solution(N):
    maps = []
    for _ in range(N):
        maps.append(input().strip())

    dr, dc = [1, -1, 0, 0], [0, 0, -1, 1]

    def bfs_three(start_v, visited):
        visited[start_v[0]][start_v[1]] = True
        queue = collections.deque([start_v])
        find = False
        while queue:
            vr, vc = queue.popleft()
            for d in range(4):
                wr, wc = vr + dr[d], vc + dc[d]
                if 0 <= wr < N and 0 <= wc < N:
                    if not visited[wr][wc] and maps[vr][vc] == maps[wr][wc]:
                        visited[wr][wc] = True
                        queue.append((wr, wc))
        return visited

    def bfs_two(start_v, visited):
        color = "B" if maps[start_v[0]][start_v[1]] == "B" else "RG"
        visited[start_v[0]][start_v[1]] = True
        queue = collections.deque([start_v])
        while queue:
            vr, vc = queue.popleft()
            for d in range(4):
                wr, wc = vr + dr[d], vc + dc[d]
                if 0 <= wr < N and 0 <= wc < N:
                    if not visited[wr][wc] and maps[wr][wc] in color:
                        visited[wr][wc] = True
                        queue.append((wr, wc))
        return visited

    cnt_two, cnt_three = 0, 0
    visited_two = [[False for _ in range(N)] for _ in range(N)]
    visited_three = [[False for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visited_three[r][c]:
                cnt_three += 1
                visited_three = bfs_three((r, c), visited_three)
            if not visited_two[r][c]:
                cnt_two += 1
                visited_two = bfs_two((r, c), visited_two)
    return f"{cnt_three} {cnt_two}"


print(solution(int(input().strip())))
