import sys; input=sys.stdin.readline;
t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    data=list(map(int,input().split()))

    if n==m:
        print(1) if sum(data[:m])<k else print(0)
        continue
    
    start=0; end=0; interval=0; ans=0; tmp_cnt=0
    for start in range(n):
     
        while end<n+(m-1) and tmp_cnt<m:
            interval+=data[end%n]
            end+=1
            tmp_cnt+=1

    
        if interval<k:
            ans+=1
        interval-=data[start]
        tmp_cnt-=1
    print(ans)