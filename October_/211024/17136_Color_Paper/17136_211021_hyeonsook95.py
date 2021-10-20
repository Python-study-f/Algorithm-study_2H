# https://jjangsungwon.tistory.com/74
# https://dongsik93.github.io/algorithm/2019/09/03/algorithm-boj-17136/
def solution():
    maps = [list(map(int, input().split())) for _ in range(10)]
    visited = [[False for _ in range(10)] for _ in range(10)]
    papers = [0, 5, 5, 5, 5, 5]

    def cover(start_r, start_c, size, value):
        for r in range(start_r, start_r + size):
            for c in range(start_c, start_c + size):
                visited[r][c] = value
        return

    def dfs(min_used, used, uncovered):
        if not uncovered:
            return min(min_used, used)
        if min_used <= used or not sum(papers):
            return min_used

        for r in range(10):
            for c in range(10):
                if maps[r][c] == 1 and not visited[r][c]:
                    for size in range(5, 0, -1):
                        if papers[size] > 0 and r + size <= 10 and c + size <= 10:

                            is_covered = True
                            for sr in range(r, r + size):
                                for sc in range(c, c + size):
                                    if maps[sr][sc] == 0 or visited[sr][sc]:
                                        is_covered = False
                                        break
                                if not is_covered:
                                    break

                            if is_covered:
                                papers[size] -= 1
                                cover(r, c, size, True)
                                min_used = min(
                                    min_used,
                                    dfs(min_used, used + 1, uncovered - (size ** 2)),
                                )
                                papers[size] += 1
                                cover(r, c, size, False)
                    return min_used

    answer = dfs(26, 0, sum(map(sum, maps)))
    if answer > 25:
        return -1
    return answer


if __name__ == "__main__":
    print(solution())
