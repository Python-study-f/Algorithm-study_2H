data=["[","(","{"]	
def check(temp):
    arr=[]
    for i in range(len(temp)):
        if temp[i] in data:
            arr.append(temp[i])
        else:
            if len(arr)==0:
                return False
            else:
                now=arr.pop()
                if now == "[" and temp[i] == "]":
                    continue;
                elif now == "(" and temp[i] == ")":
                    continue;
                elif now == "{" and temp[i] == "}":
                    continue;
                else:
                    return False;
    if len(arr)!=0:
        return False
    return True

def solution(s):
    answer=0
    temp=s
    
    for i in range(len(s)):
        temp=temp[1:]+temp[0]
        if check(temp):
            answer+=1
    return answer