n,h=map(int,input().split())
data1=[0]*(h+1); data2=[0]*(h+1)

for i in range(n):
    if i%2!=0:
        data1[int(input())]+=1
    else:
        data2[h-int(input())+1]+=1
        
        
for i in range(h-1,0,-1):
    data1[i]+=data1[i+1]
    
for i in range(2,h+1):
    data2[i]+=data2[i-1]
    
ans=[0]*(h+1)
for i in range(1,h+1):
    ans[i]=data1[i]+data2[i]
    
ans=ans[1:]
tmp=min(ans)
print(tmp,ans.count(tmp))