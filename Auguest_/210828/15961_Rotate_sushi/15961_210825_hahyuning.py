# n: 놓인 접시의 수, d: 초밥의 가짓수, k: 연속해서 먹는 접시의 수, c: 쿠폰 번호
n, d, k, c = map(int, input().split())
a = [int(input()) for _ in range(n)]
a += a[:k]

# 초밥의 종류
sushi = dict()
for x in a:
    sushi[x] = 0
sushi[c] = 0

cnt = 0 # 먹은 초밥의 개수
kind = 0 # 먹은 초밥의 종류
lt, rt = 0, 0
ans = 0

while lt < len(a) and rt < len(a):
    # 먹은 초밥의 개수가 k개를 초과한 경우
    if cnt >= k:
        sushi[a[lt]] -= 1
        if sushi[a[lt]] == 0:
            kind -= 1
        lt += 1
        cnt -= 1
    else:
        if sushi[a[rt]] == 0:
            kind += 1
        sushi[a[rt]] += 1
        rt += 1
        cnt += 1

    # 최댓값 갱신
    if kind >= ans:
        ans = kind
        if sushi[c] == 0:
            ans += 1

print(ans)