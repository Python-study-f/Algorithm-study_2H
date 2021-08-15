T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    sent = list(input().strip().replace('?','.').replace('!','.').split('.'))
    res = []
    for words in sent:
        if words:
            tmp = words.split()
            cnt = 0
            for word in tmp:
                if word[0].isupper():
                    if not any(letter.isdigit() for letter in word) and not any(letter.isupper() for letter in word[1:]):
                        cnt += 1
            res.append(cnt)
    print('#{} {}'.format(test_case, ' '.join(map(str, res))))
    

    
#all 함수 : all(iterable) 함수는 인자로 받은 반복 가능한 자료형(iterable)의 모든 요소가 참(True)이면 참(True)을 반환하는 함수 입니다.
#any 함수 : any(iterable) 함수는 인자로 받은 반복가능한 자료형(iterable)중 단 하나라도 참(True)이 있으면 참(True)를 반환하는 함수 입니다. 반대로 모든 요소가 거짓(False)인 경우에만 거짓(False)을 반환합니다.
#출처: https://blockdmask.tistory.com/430 [개발자 지망생]

