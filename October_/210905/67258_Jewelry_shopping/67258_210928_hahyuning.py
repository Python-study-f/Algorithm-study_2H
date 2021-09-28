from collections import defaultdict

def solution(gems):
    n = len(set(gems))
    lt = 0
    rt = 0

    ans = []
    check = defaultdict(int)
    check[gems[0]] += 1
    while lt < len(gems) and rt < len(gems):
        # n개의 보석을 다 찾으면 lt += 1
        if len(check) == n:
            ans.append([lt + 1, rt + 1])

            if check[gems[lt]] <= 1:
                del check[gems[lt]]
            else:
                check[gems[lt]] -= 1
            lt += 1

            if lt > rt:
                rt = lt
        else:
            rt += 1
            if rt < len(gems):
                check[gems[rt]] += 1

    ans.sort(key=lambda x:(x[1] - x[0], x[0]))
    return ans[0]