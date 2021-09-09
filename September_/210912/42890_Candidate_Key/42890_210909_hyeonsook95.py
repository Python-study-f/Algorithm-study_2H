from itertools import combinations


def solution(relation):
    R, C = len(relation), len(relation[0])

    keys = []
    for n in range(1, C + 1):
        keys.extend(list(map(list, combinations(list(range(C)), n))))

    # 유일성: 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 함.
    unique_keys = []
    for key in keys:
        check_keys = []
        for r in range(R):
            tmp = []
            for k in key:
                tmp.append(relation[r][k])
            if tmp not in check_keys:
                check_keys.append(tmp)
        if len(check_keys) == R:
            unique_keys.append(key)

    # 최소성: 키를 구성하는 속성의 개수가 최소가 되어야 함.
    minimal_keys = unique_keys[::]
    for u_key in unique_keys:
        if u_key not in minimal_keys:
            continue
        tmp_keys = [u_key]
        for m_key in minimal_keys:
            if not set(u_key).issubset(set(m_key)):
                tmp_keys.append(m_key)
        minimal_keys = tmp_keys[::]
    return len(minimal_keys)
