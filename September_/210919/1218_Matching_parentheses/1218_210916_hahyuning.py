from collections import defaultdict

for tc in range(1, 11):
    n = int(input())
    s = input()

    a = {")": "(", "}":"{", "]":"[", ">":"<"}
    check = defaultdict(int)
    for x in s:
        if x in a.values():
            check[x] += 1
        else:
            check[a[x]] -= 1

            if check[a[x]] < 0:
                print("#{} {}".format(tc, 0))
                break
    else:
        for val in check.values():
            if val != 0:
                print("#{} {}".format(tc, 0))
                break
        else:
            print("#{} {}".format(tc, 1))
