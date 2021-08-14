# 풀이 1.
"""
ans = [0 for _ in range(len(query))]
info_st = []
query_st = []

# 나누기
for i in range(len(info)):
    info_st.append(info[i].split())

# and 제거
for i in range(len(query)):
    query_st.append(query[i].split())
    while len(query_st[i]) > 5:
        query_st[i].replace('and','')


for i in range(len(info_st)):
    for j in range(len(query_st)):
        check = 0
        # dictionary 에서 key,value 처럼 구별
        for k in range(4):
            if info_st[i][k] != query_st[j][k]:
                if query_st[j][k] !=  '-': # - 처리
                    check = 1
                    break
        if check == 0:
            if int(info_st[i][4]) >= int(query_st[j][4]):
                ans[j] += 1
print(ans)
"""

# 풀이 2.
# 효율성에 다 터짐. 방법을 찾아야함.
from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    info_st = []
    info_dic = {}

    for i in range(len(info)):
        info_st = info[i].split()
        key = info_st[:len(info_st)-1]
        value = int(info_st[-1])

        # Combination으로 key 조합 만들기
        for j in range(5):
            for comb in combinations(key,j):
                tmp = ''.join(comb)

                if info_dic.get(tmp) is None:
                    info_dic[tmp] = [int(value)] # 값 초기화
                else:
                    info_dic[tmp].append(int(value)) # 값 추가

    for k in info_dic.keys():
        info_dic[k] = sorted(info_dic[k]) # 이진탐색을 위한 정렬

    result = []
    for q in query:
        q = q.replace('and','').split() # and 삭제

        while '-' in q: # - 제거
            q.remove('-')

        q_key, q_value = ''.join(q[:len(q)-1]), int(q[-1])

        if not q_key in info_dic:
            result.append(0)
        else:
            values = info_dic[q_key]
            result.append(len(values) - bisect_left(values, q_value))

    return result