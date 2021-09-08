from itertools import combinations

def solution(relation):
    # 유일성: 릴레이션에 있는 모든 튜플에 대해 유일하게 식별
    # 최소성: 유일성을 만족하는 데 꼭 필요한 속성들로만 구성

    n = len(relation)
    m = len(relation[0])

    # 가능한 모든 후보키의 집합
    all_key = []
    for i in range(1, m + 1):
        tmp = [set(x) for x in combinations([j for j in range(m)], i)]
        all_key += tmp

    # 1. 유일성 검증
    unique_key = []
    for key in all_key:
        check = set()
        # i번째 학생에 대해 해당 키로 유일하게 식별 가능한지 확인
        for i in range(n):
            tmp = ""
            for x in key:
                tmp += relation[i][x]
            check.add(tmp)

        if len(check) == n:
            unique_key.append(key)

    # 2. 최소성 검증
    not_min_key = []
    for k1 in unique_key:
        for k2 in unique_key:
            # k1이 k2의 부분집합이 될 경우 k2는 최소성 만족 X
            if k1.issubset(k2) and k1 != k2:
                if k2 not in not_min_key:
                    not_min_key.append(k2)

    return len(unique_key) - len(not_min_key)