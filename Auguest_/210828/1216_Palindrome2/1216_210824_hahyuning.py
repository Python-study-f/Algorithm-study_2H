# 팰린드롬 체크
def check(s):
    if s == s[::-1]:
        return len(s)

    ans = 0
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if s[i:j] == s[i:j][::-1]:
                ans = max(ans, len(s[i:j]))
    return ans


for _ in range(10):
    tc = int(input())
    a = [input() for _ in range(100)]
    ans = 1

    # 행검사
    for i in range(100):
        s = a[i]
        ans = max(ans, check(s))

    # 열검사
    for j in range(100):
        s = ""
        for i in range(100):
            s += a[i][j]
        ans = max(ans, check(s))

    print("#{}".format(tc), end=" ")
    print(ans)