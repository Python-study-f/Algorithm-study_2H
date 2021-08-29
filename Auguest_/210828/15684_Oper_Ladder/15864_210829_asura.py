# 공부 링크 : https://coreenee.github.io/2020/07/02/%EB%B0%B1%EC%A4%8015684(%EC%82%AC%EB%8B%A4%EB%A6%AC-%EC%A1%B0%EC%9E%91)/
# 영상 링크 : https://www.youtube.com/watch?v=QHHi2nYg7c4
# 이 블로그에 여러 문제들이 풀려있다. 필기를 한 흔적들이 있기 때문에 앞으로 그려가면서 공부하면 도움 될 것 같다.

# 사다리에 가로선을 놓는 함수
def dfs(start, cnt):
    ans = 0

N, M, H = map(int, input().split())
ladder = [[0] * (N+1) for _ in range(H+1)]
ret = 4

def check():
    flag = True

    for n in range(1,N+1):
        pos = n

        for m in range(H+1):
            if ladder[m][pos] == 1:
                pos += 1
            elif ladder[m][pos-1] == 1:
                pos -= 1

        if pos != n:
            flag = False
            return flag
    return flag

def dfs(cnt,x,y):
    global ret
    if cnt >= ret: # 내가 찾은 값 < 새로 발견된 값 -> 종료하면 됨
        return

    if check(): # 현재 조건에 만족하는지 체크
        ret = cnt
        return

    if cnt == 3: # 다음 dfs가 4이기때문에 여기서 종료
        return

    for n in range(x,H+1):
        for m in range(y,n):
            if ladder[n][m] == 0 and ladder[n][m-1] == 0 and ladder[n][m+1] == 0: # 선이 이미 그어져 있지 않으면,
                ladder[n][m] = 1
                dfs(cnt+1,n,m)
                ladder[n][m] = 0
        y = 1




for i in range(M):
    a,b = map(int,input().split())
    ladder[a][b] = 1

dfs(0, 1, 1) # 첫번째 파라미터 : 몇번의 선을 그었는지 / 2,3 번째 : 시작점 좌표

if ret == 4:
    print(-1)


"""
첫번째 그림을 보면 파란색 글씨는 배열에서의 인덱스를 가르키고, 
빨간색 글씨는 사다리 타기 할 때의 점의 좌표의 느낌으로 생각하면 되겠다. 
자, 그러면 만약에 다리가 설치되있고, 또 앞으로 설치를 할 때는 어떤식으로 표현을 해야할까? 
두번째 그림을 한번 봐보자. 실선으로 진하게 그려진 부분이 다리가 연결되었다는 뜻이다. (0,0) 좌표를 큐에 넣어서 표현을 해도 되지만, 
시간을 줄이기 위해 칠해진 부분을 네모의 아랫변으로 보고 왼쪽위 꼭지점이 1이면 다리가 있다는 뜻이 되겠다. 
한마디로 말하자면, flag를 담고 있는 map_list가 있다면 map_list[0][0] 이 1이라는 뜻이다. 
이러한 자료구조로 백트래킹과 재귀를 이용해서 풀어주면 되겠다!
"""