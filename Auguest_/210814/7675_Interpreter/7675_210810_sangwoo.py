a = int(input())
for i in range(a):
    b = int(input())
    sentence = list(map(str, input().split()))
    count = 0
    ans = []
    for word in sentence:
        if word[-1] == '.' or word[-1] == '!' or word[-1] == '?':
            if word[0].isupper():
                if word[1:len(word)-1].isalpha() and word[1:].islower():
                    count += 1
                ans.append(count)
                count = 0
        else:
            if word[0].isupper() and word.isalpha() and word[1:].sislower():
                count += 1
    print('#{}'.format(i+1),end=" ")
    print(*ans)
            
                    
                    
            
