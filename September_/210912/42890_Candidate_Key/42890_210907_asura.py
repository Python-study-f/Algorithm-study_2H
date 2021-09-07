"""
https://johnyejin.tistory.com/129 순차적으로 생각하는 방향이 좋았음
https://whwl.tistory.com/104
https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%ED%9B%84%EB%B3%B4%ED%82%A4
정리 잘해둔 블로그

"""
from itertools import combinations
from collections import  deque

def solution(relation):

    answer = 0
    cobm = [i for i in range(len(relation[0]))]
    tot = [] # 모든 컬럼 조합 리스트

    if len(relation) > 0:
        N = len(relation)
        M = len(relation[0])

        # 전체 조합 찾기
        for i in range(1,M+1):
            tot.extend(list(combinations(cobm,i)))
            # [{0}, {1}, {2}, {3}, {0, 1}, {0, 2}, {0, 3}, {1, 2}, {1, 3}, {2, 3}, {0, 1, 2}, {0, 1, 3}, {0, 2, 3}, {1, 2, 3}, {0, 1, 2, 3}]

        # 1. 유일성 체크
        uniq = deque()  # 유일성 만족 리스트
        for comb in tot:
            SET = set()

            for i in range(N):
                tmp = ''
                for j in comb:
                    tmp += relation[i][j]
                SET.add(tmp)

            if len(SET) == N:
                uniq.append(comb)

        # 2. 최소성 체크
        while uniq:
            temp = uniq.popleft()
            answer += 1
            new = deque()
            for i in uniq:
                if len(set(i)-set(temp)) != len(i)-len(temp):
                    new.append(i)
            uniq = new
        return answer
