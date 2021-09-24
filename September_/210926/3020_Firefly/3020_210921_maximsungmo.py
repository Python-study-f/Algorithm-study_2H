# 개똥벌레 3090 백준

bottom = []
top = []

n, h = map(int, input().split())

memo = {}
for _ in range(h):
    memo.setdefault(_ + 1, 0)


def check(height, is_even):
    if not is_even:
        for hol in range(1, height + 1, +1):
            memo[hol] = memo[hol] + 1
    else:
        for zzak in range(h - height, h, +1):
            memo[zzak] = memo[zzak] + 1


for i in range(n):
    k = int(input())
    if i % 2 == 0:
        check(k, True)
    else:
        check(k, False)

sorted_dict = sorted(memo.items(), key = lambda item: item[1])
print(sorted_dict)

print(memo)
