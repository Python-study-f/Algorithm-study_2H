# 회문2 1216 SW expert

for _ in range(10):
    t = int(input())
    arr = [list(input()) for _ in range(100)]
    maxPalindrome = 0
    rotArr = list(map(list, zip(*arr)))

    for i in range(100):
        for j in range(100):
            for k in range(100 - j):
                tmp = arr[i][j : j + k + 1]
                tmp2 = rotArr[i][j : j + k + 1]
                if tmp == tmp[::-1]:
                    maxPalindrome = max(len(tmp), maxPalindrome)
                if tmp2 == tmp2[::-1]:
                    maxPalindrome = max(len(tmp2), maxPalindrome)

    print(f"#{t} {maxPalindrome}")
