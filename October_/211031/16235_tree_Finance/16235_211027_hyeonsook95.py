# pypy3 640ms
def solution(N, M, K):
    # S2D2가 각 칸에 추가하는 양분의 양
    a = [list(map(int, input().strip().split())) for _ in range(N)]

    maps = [[[5, []] for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        # 상도가 심은 나무의 정보 (x, y, z: 나이)
        r, c, z = map(int, input().strip().split())
        maps[r - 1][c - 1][1].append(z)

    def spring_and_summer():
        for r in range(N):
            for c in range(N):
                if maps[r][c][1]:
                    food = maps[r][c][0]
                    trees = sorted(maps[r][c][1], reverse=True)

                    new_trees = []
                    while trees and food:
                        if trees[-1] <= food:
                            new_trees.append(trees.pop())
                            food -= new_trees[-1]
                            new_trees[-1] += 1
                        else:
                            break

                    food += sum(map(lambda t: t // 2, trees))
                    maps[r][c] = [food, new_trees]

    def autumn_and_winter():
        dr = [-1, -1, -1, 0, 0, 1, 1, 1]
        dc = [-1, 0, 1, -1, 1, -1, 0, 1]

        for r in range(N):
            for c in range(N):
                maps[r][c][0] += a[r][c]
                if maps[r][c][1]:
                    for tree in maps[r][c][1]:
                        if tree % 5 == 0:
                            for d in range(8):
                                wr, wc = r + dr[d], c + dc[d]
                                if -1 < wr < N and -1 < wc < N:
                                    maps[wr][wc][1].append(1)

    for _ in range(K):
        # 봄 & 여름
        spring_and_summer()
        # 가을 & 겨울
        autumn_and_winter()

    count = 0
    for r in range(N):
        for c in range(N):
            count += len(maps[r][c][1])

    return count


if __name__ == "__main__":
    print(solution(*map(int, input().strip().split())))
