# places의 각 행은 하나의 대기실 구조를 나타낸다.
# 각 대기실이 거리두기 규칙을 잘 지키고 있다면 1, 지키지 않고 있다면 0을 나타내라.


from collections import deque


def solution(places):
    answer = []

    def bfs(p, graph):
        dr, dy = [1, -1, 0, 0], [0, 0, -1, 1]
        visited = [[-1 for _ in range(5)] for _ in range(5)]

        queue = deque([p])
        visited[p[0]][p[1]] = 0

        while queue:
            vr, vc = queue.popleft()
            for r, c in list(zip(dr, dy)):
                wr, wc = vr + r, vc + c
                if (
                    -1 < wr < 5
                    and -1 < wc < 5
                    and visited[wr][wc] == -1
                    and graph[wr][wc] != "X"
                ):
                    visited[wr][wc] = visited[vr][vc] + 1
                    queue.append((wr, wc))
                    if graph[wr][wc] == "P" and visited[wr][wc] < 3:
                        return False
        return True

    for place in places:
        person = []

        # 대기자 위치
        for r in range(5):
            for c in range(5):
                if place[r][c] == "P":
                    person.append((r, c))

        if all(map(lambda p: bfs(p, place), person)):
            answer.append(1)
        else:
            answer.append(0)
    return answer
