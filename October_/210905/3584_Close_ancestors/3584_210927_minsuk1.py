t=int(input())
for _ in range(t):
    n=int(input())
    p=[0 for _ in range(n+1)]
    for _ in range(n-1):
        a,b=map(int,input().split())
        p[b]=a
    
    a,b=map(int,input().split())
    parent_a=[a]
    parent_b=[b]
    
    while p[a]!=a:
        parent_a.append(p[a])
        a=p[a]
        
    while p[b]!=b:
        parent_b.append(p[b])
        b=p[b]
        
    first=len(parent_a)-1
    second=len(parent_b)-1
    while parent_a[first]==parent_b[second]:
        first-=1
        second-=1
    print(parent_a[first+1])