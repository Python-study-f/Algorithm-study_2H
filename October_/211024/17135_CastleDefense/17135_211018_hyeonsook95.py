# 29200kb 648ms
from itertools import combinations


def solution(N, M, D):
    maps = [list(map(int, input().split())) for _ in range(N)]
    targets = []
    for r in range(N):
        for c in range(M):
            if maps[r][c] == 1:
                targets.append((r, c))

    def game(archers):
        cnt, move = 0, 0
        killed = [False] * len(targets)
        # 적이 없을 때까지 반복함
        while sum(killed) != len(killed):
            killed_list = []
            # 궁수가 공격함
            for ac in archers:
                dists = []
                for idx, target in enumerate(targets):
                    if not killed[idx]:
                        # 맵을 나가면 죽음
                        if target[0] + move >= N:
                            killed[idx] = True
                            continue
                        dist = abs(N - (target[0] + move)) + abs(ac - target[1])
                        # 거리가 D 이하일 때만 죽일 수 있음
                        if dist <= D:
                            dists.append((dist, target[1], idx))
                if dists:
                    killed_list.append(sorted(dists)[0][-1])
            # 적을 죽임
            cnt += len(set(killed_list))
            for k in set(killed_list):
                killed[k] = True
            # 적이 이동함
            move += 1
        return cnt

    cnt = 0
    targets.sort(key=lambda x: (-x[0], x[1]))
    for archers in combinations(range(M), 3):
        cnt = max(cnt, game(archers))
    return cnt


# https://www.acmicpc.net/source/34068532
# 궁수가 쏠 수 있는 거리에 따라 좌측, 전방, 우측 순으로 탐색하여 적을 죽임
# 위에서 한칸 내려오는게 아니라 궁수가 한 칸 전진함

if __name__ == "__main__":
    N, M, D = map(int, input().split())
    print(solution(N, M, D))
