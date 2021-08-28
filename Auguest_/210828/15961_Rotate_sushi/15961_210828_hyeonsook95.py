import sys

input = sys.stdin.readline


def solution(N, D, K, C):
    kinds = 0
    sushi = [0 for _ in range(D + 1)]
    dishes = []
    for _ in range(N):
        dishes.append(int(input().strip()))

        if _ < K:
            if sushi[dishes[-1]] == 0:
                kinds += 1
            sushi[dishes[-1]] += 1

    if sushi[C] == 0:
        sushi[C] += 1
        kinds += 1

    i = 0
    j = i + (K - 1)
    max_kinds = 0
    while i < N:
        i += 1
        sushi[dishes[i - 1]] -= 1
        if sushi[dishes[i - 1]] == 0:
            kinds -= 1

        j = (i + K - 1) % N
        sushi[dishes[j]] += 1
        if sushi[dishes[j]] == 1:
            kinds += 1

        if sushi[C] == 0:
            sushi[C] += 1
            kinds += 1
        max_kinds = max(max_kinds, kinds)

    return max_kinds


N, D, K, C = map(int, input().split())

print(solution(N, D, K, C))
