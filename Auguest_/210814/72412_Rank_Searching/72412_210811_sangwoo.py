from itertools import combinations
from bisect import bisect_left


def solution(info, querys):
    answer = []
    dic = {}

    for i in range(len(info)):
        infol = info[i].split()  
        key = infol[0:4]  
        value = int(infol[4])

        for j in range(5):  
            for c in combinations(key, j):
                tmp = ''.join(c)
                if tmp in dic:
                    dic[tmp].append(value) 
                else:
                    dic[tmp] = [value]

    for k in dic:
        dic[k].sort() 

    for q in querys:  
        query = q.split(' ')
        qkey = query[:-1]
        qvalue = int(query[-1])

        while 'and' in qkey:  
            qkey.remove('and')
        while '-' in qkey:  
            qkey.remove('-')
        qkey = ''.join(qkey)  

        if qkey in dic:  
            scores = dic[qkey]
            if scores:  
                enter = bisect_left(scores, qvalue)
                answer.append(len(scores) - enter)
        else:
            answer.append(0)

    return answer
