for t in range(int(input())):
    n=int(input())
    data=input()
    
    end_point=['?', '!']
    for i in data:
        if i in end_point:
            data=data.replace(i,'.')
    data=data.split('.')[0:-1]
    
    
    ans=[]; nums=[str(i) for i in range(1,11)]
    for i in data:
        tmp=i.split()
        cnt=0
        for j in tmp:
            if len(j)==1 and j.isupper():
                cnt+=1
            elif j[0].isupper() and j[1:].islower() and j.isalpha():
                cnt+=1
        ans.append(cnt)
        
    print('#{} {}'.format(t+1, ' '.join(map(str, ans))))