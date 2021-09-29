from collections import Counter

r,c,k = map(int,input().split())
r,c = r-1, c-1 # 인덱스 처리
data = [list(map(int,input().split())) for _ in range(3)]

def rc():
    max_len = 0
    row = len(data)
    ret = []

    for tmp in data:
        tmp = Counter(tmp) # tmp를 Counter 딕셔너리로 변환
        del (tmp[0]) # 리스트에 0 제거
        tmp = sorted(tmp.items(), key=lambda x: (x[1], x[0])) # 첫번째로는 count 횟수로 정렬, 그 후 두번째 정렬조건은 key 값으로

        check = []
        for tm in tmp:
            check.extend(tm)
            if len(check) == 100: # 100번 넘어가면 종료
                break

        max_len = max(max_len,len(check))
        ret.append(check)

    for tm in ret:
        tm += [0] * (max_len-len(tm)) # 가장 큰 길이까지 0으로 채워넣기

    return ret

for t in range(101):
    if r < len(data) and c < len(data[0]) and data[r][c] == k: # 정답일 경우
        print(t)
        break

    if len(data) < len(data[0]): # 돌리고 돌리고
        data = list(zip(*data))
        data = rc()
        data = list(zip(*data))
    else: # 아니면 진행
        data = rc()
else:
    print(-1)


