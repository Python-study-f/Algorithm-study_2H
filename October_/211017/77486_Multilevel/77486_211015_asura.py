def solution(enroll, referral, seller, amount):
    ans = [0] * len(enroll)
    graph = {}

    for i in range(len(enroll)):
        graph[enroll[i]] = i

    for i in range(len(seller)):
        people = seller[i]
        price = amount[i] * 100

        while True:
            node = graph[people]
            div = price // 10
            ans[node] += price - div

            price = div
            people = referral[node]

            if people == "-": break
            if div == 0: break

    return ans