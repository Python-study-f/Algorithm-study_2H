"""
1. 자석을 움직일 필요X. 개수를 체크해서 계산하는 게 좋아보임
2. 행은 볼 필요 없기, 열만 계산해서 하면 빠를것으로 보임.
3. 1-2 순서는 stack을 이용. 1나오면 스택에 넣어 2나올때 pop하고, 교착상태 + 1로 체크
"""
T = 10

for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    tot_cnt = 0

    for i in range(N): # data[row][col]
        st = []
        row, col = 0, i

        while row < N:
            if not st and data[row][col] == 1: # N을 가르키는 극성일 경우
               st.append(1)
            elif st and data[row][col] == 2: # S를 가르키는 극성일 경우
                tot_cnt += st.pop()

            row += 1 # 다음 열 진행

    print("#{} {}".format(tc, tot_cnt))