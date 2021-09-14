def alphabet(start, cnt):
    global ans
    # 종료조건: 알파벳 k개를 다 배운 경우
    if cnt == k:
        read_cnt = 0
        for word in words_set:
            for w in word:
                if not learn[ord(w) - ord("a")]:
                    break
            else:
                read_cnt += 1
        ans = max(read_cnt, ans)
        return

    for i in range(start, 26):
        if learn[i] == False:
            learn[i] = True
            alphabet(i + 1, cnt + 1)
            learn[i] = False

n, k = map(int, input().split())
words = [set(input()) for _ in range(n)]

if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    learn = [False] * 26
    for x in ["a", "n", "t", "c", "i"]:
        learn[ord(x) - ord("a")] = True
    k -= 5

    words_set = []
    for word in words:
        tmp = set()
        for w in word:
            if w not in ["a", "n", "t", "c", "i"]:
                tmp.add(w)
        words_set.append(tmp)

    ans = 0
    alphabet(0, 0)
    print(ans)
