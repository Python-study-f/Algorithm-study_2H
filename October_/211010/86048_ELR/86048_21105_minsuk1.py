def solution(enter, leave):
    ans = [0]*(len(enter)+1)
    for i in range(1,len(leave)+1):
        a,b=enter.index(i), leave.index(i)
        early=leave[:b]
        for j in early:
            a_=enter.index(j)
            b_=leave.index(j)
            if a_>a:
                ans[i]+=1
                ans[j]+=1
            else:
                for k in early[:b_]:
                    e3 = enter.index(k)
                    if e3 > a_ and e3 > a:
                        ans[i]+=1
                        ans[j]+=1
    return ans[1:]