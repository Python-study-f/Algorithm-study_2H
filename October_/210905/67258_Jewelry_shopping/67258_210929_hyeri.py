# two pointer 
# 참고 : https://bladejun.tistory.com/95

def solution(gems):
    answer = [1, len(gems)]   
    n = len(set(gems))
    dic = {}
    
    s, e = 0, 1
    standard = gems[s]
    dic[gems[s]] = s
    if len(set(gems)) == 1:
        return [1, 1]
    
    while e < len(gems):
        dic[gems[e]] = e
        if standard == gems[e]:
            new = sorted(dic.keys(), key=lambda x: dic[x])[0]
            standard = new
            s = dic[new]
        
        if len(dic.keys()) == n:
            answer = [s+1, e+1] if answer[1]-answer[0] > e-s else answer
        e += 1
    return answer



''' dictionary 를 사용하지 않을 경우, 효율성에서 일부 시간 초과 발생, 총점 : 77.8 점
from collections import deque
def solution(gems):
    answer = [0, len(gems)]
    e, n, cnt, s = 0, len(set(gems)), 0, 0
    gem = deque()
    while e < len(gems):
        if gems[e] not in gem:
            cnt += 1
        gem.append(gems[e])
        e += 1
        while cnt == n:
            if (answer[1] - answer[0]) > (e - s - 1):
                answer[1] = e
                answer[0] = s + 1
            m = gem.popleft()
            if m not in gem:
                cnt -= 1
            s += 1
    return answer 
    '''
