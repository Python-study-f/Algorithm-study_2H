# window + memorize
# 41320kb 544ms
def solution(N, M, K):
    homes = list(map(int, input().split()))
    dp = sum(homes[:M])
    if N == M:
        return 1 if dp < K else 0

    cnt = 0
    right = M - 1
    for left in range(N):
        if dp < K:
            cnt += 1
        right = (right + 1) % N
        dp = dp + homes[right] - homes[left]
    return cnt


if __name__ == "__main__":
    for _ in range(int(input().strip())):
        N, M, K = map(int, input().split())
        print(solution(N, M, K))
