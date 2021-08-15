# 1. 단순 리스트로 풀기 - 정확도 100 효율성 0 

def solution(info, query):
    answer = []
    inf = []
    for i in info:
        inf.append(i.split())

    for q in query:
        result = 0
        ql = q.split()
        qs = len(ql)
        for person in inf:
            chk = True
            for qi in range(0, qs-1, 2):
                if ql[qi] == '-':
                    continue
                if ql[qi] not in person:
                    chk = False
                    break
            if int(ql[-1]) > int(person[-1]):
                chk = False
            if chk:
                result += 1
        answer.append(result)

    return answer
  
  
  
  
  # 2. 이진탐색으로 풀라고 하는데 공부중
