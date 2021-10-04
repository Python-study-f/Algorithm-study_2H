t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))

    if n == m:
        print(1 if sum(a) < k else 0)
        continue

    a += a
    s = sum(a[:m])
    rt = m - 1
    ans = 0
    for lt in range(n):
        if s < k:
            ans += 1

        s -= a[lt]
        rt += 1
        s += a[rt]

    print(ans)