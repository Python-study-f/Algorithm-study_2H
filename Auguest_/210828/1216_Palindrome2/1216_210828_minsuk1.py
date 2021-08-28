def check(x):
    if x==x[::-1]:
        return True

for t in range(1, 11):
    a=int(input())
    list1 = [list(input()) for _ in range(100)]
    list2 = list(zip(*list1))

    result = 0
    for k in range(100, 0, -1):
        if result >= k:
            break
        for i in range(100):
            if result == k:
                break
            for j in range(100-k+1):
                if check(list1[i][j:j+k]) or check(list2[i][j:j+k]):
                    result=k
                    break
            
    print("#{} {}".format(a, result))