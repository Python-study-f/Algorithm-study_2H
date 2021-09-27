import copy
import sys

input = sys.stdin.readline

dx, dy = [0,0,-1,1], [-1,1,0,0] # L,R,U,D

# 0 1 2 3 = 상 하 좌 우 / 첫번째 인덱스 계산 편하기 위해 비워둠
direction = [ [], [[0],[1],[2],[3]], [[0,1], [2,3]], [[2,0], [2,1], [1,3], [3,0]],
              [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]], [[0,1,2,3]] ]
INF = int(1e9)

def watch(x, y, Direct, tmp):
    for d in Direct:
        nx = x
        ny = y
        while True:
            nx, ny = nx + dx[d], ny +dy[d]

            if 0 <= nx < N and 0 <= ny < M and tmp[nx][ny] != 6:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = '#'
            else:
                break

def dfs(cctv_load,cnt):
    global ans

    temp = copy.deepcopy(cctv_load) # 전체 map을 temp에에 사하고
    if cnt == cctv_cnt: # 만약 지금까지 센 cctv 갯수가 전체 cctv갯수와 같다면,
        check = 0

        for a in temp: # 여기서 a는 리스트
            check += a.count(0) # 0 개수 카운트
        ans = min(ans,check)
        return

    x,y,cctv = st[cnt]
    for direct in direction[cctv]:
        watch(x, y, direct, temp)
        dfs(temp, cnt + 1)
        temp = copy.deepcopy(cctv_load)

N,M = map(int,input().split())
data = []
cctv_cnt = 0
st = []
ans = INF

for i in range(N):
    lst_data = list(map(int,input().split()))
    data.append(lst_data) # 리스트에 넣고

    for j in range(len(lst_data)):
        if lst_data[j] != 0 and lst_data[j] != 6 : # 0과 6을 제외한 cctv 숫자 체크
            cctv_cnt += 1
            st.append([i,j,lst_data[j]]) # stack에 cctv 좌표와 몇번 cctv인지 넣기

dfs(data,0)
print(ans)