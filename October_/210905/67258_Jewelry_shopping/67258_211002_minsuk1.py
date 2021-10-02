from collections import defaultdict
def solution(gems):
    n=len(set(gems))
    dic=defaultdict(int)
    start,end=0,0
    answer=[0,int(1e9)]
    cnt=0; isFlag = False
    
    while start<len(gems) and end<len(gems):
        if not isFlag:
            if not dic[gems[end]]:
                cnt+=1
            dic[gems[end]]+=1
            
        if cnt==n:
            dic[gems[start]]-=1
            if not dic[gems[start]]: 
                cnt-=1
            answer = min(answer, [start+1, end+1], key=lambda x: abs(x[1]-x[0]))
            start+=1
            isFlag=True
            continue
            
        isFlag = False
        end += 1  
            
    return answer