from collections import defaultdict


def solution(enroll, referral, seller, amount):
    ans = defaultdict(int)
    graph = dict()

    for i in range(len(enroll)):
        x = enroll[i]
        y = referral[i]
        graph[x] = y

    for i in range(len(seller)):
        child = seller[i]
        money = amount[i] * 100
        while money > 0:
            parent = graph[child]
            tmp = money - money // 10
            ans[child] += tmp

            money -= tmp
            child = parent
            if child == "-":
                break

    res = []
    for x in enroll:
        res.append(ans[x])
    return res