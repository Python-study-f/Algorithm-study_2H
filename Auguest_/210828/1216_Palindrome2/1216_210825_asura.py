def isPalindrome(s):
    return s == s[::-1]

T = 10

for tc in range(1,T+1):
    umm__ = int(input())
    ls = 1

    # 일반 100x100
    data = [list(input()) for _ in range(100)]

    # 돌린 100x100
    rotate_data = list(zip(*data))

    for i in range(100):
        for j in range(100):
            for k in range(100-j):

                # 일반 data 체크
                check = data[i][j:j+k+1]
                if isPalindrome(check):
                    ls = max(ls,len(check))

                # 돌린 data 체크
                check = rotate_data[i][j:j+k+1]
                if isPalindrome(check):
                    ls = max(ls,len(check))
    print("#{} {}".format(tc, ls))

