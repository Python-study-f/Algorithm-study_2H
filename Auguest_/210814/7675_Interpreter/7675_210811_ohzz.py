# 통역사 성경이 7675 SW expert

T = int(input())

for t in range(T):
    n = int(input())
    arr = []
    res = []
    string = input()
    prev = ""
    for s in string:
        prev += s
        if s == "!" or s == "?" or s == ".":
            arr.append(prev)
            prev = ""
    for sentence in arr:
        words = sentence.split()
        cnt = 0
        for word in words:
            flag = 0
            for i in word:
                if i.isupper():
                    if flag == 0:
                        flag = 1
                    else:
                        break
                if flag == 1 and i.isdigit():
                    break
            else:
                if flag == 1:
                    cnt += 1
        res.append(cnt)
    print(f"#{t+1}", end=" ")
    for i in range(len(res)):
        print(res[i], end=" ")
    print()
