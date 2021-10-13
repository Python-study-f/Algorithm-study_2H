# bfs + dp / 928 ms / 174608KB / pypy3
# bfs로 기본적으로 하면 시간 초과하는 것을 확인할 수 있다.
# 근데 문제에서 상하좌우에서 큰 값이 아니면 움직이지 않기 때문에,
# 이 성징를 이용해 전체 값을 정렬하고 큰값부터 갈 수 있는 길의 수를 체크하면
# 작은 값을 가지고 길을 이동할 때 큰 값을 이용할 수 있다고 판단.

import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

N = int(input())
ans = 0
data = [] # 대나무 값과 x,y 좌표 구하기.
forest = [] # 대나무 숲

for i in range(N):
    lst = list(map(int,input().split()))
    for j in range(N):
        data.append([lst[j],i,j]) # 대나무 양 x,y
    forest.append(lst)

data.sort(key= lambda k:k[0],reverse=True) # 첫번째 value로 정렬, 큰값부터 구하기 위해 내림차순 정렬

dp = [[1 for _ in range(N)] for _ in range(N)]

for i in data:
    value, x, y = i

    tmp = []
    for d in range(4):
        nx,ny = x + dx[d], y + dy[d]

        if 0 <= nx < N and 0 <= ny < N:
            if forest[x][y] < forest[nx][ny]:
                tmp.append(dp[nx][ny])
    if len(tmp) != 0:
        dp[x][y] = max(tmp) + 1

    ans = max(ans,dp[x][y])

print(ans)

#dfs + dp / 1104ms / 278732KB / python3
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x,y):
    if dp[x][y]:
        return dp[x][y]

    dp[x][y] = 1
    for d in range(4):
        nx,ny = x + dx[d], y + dy[d]

        if 0 <= nx < N and 0 <= ny < N:
            if data[x][y] < data[nx][ny]:
                dp[x][y] = max(dp[x][y],dfs(nx,ny) + 1)
    return dp[x][y]

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(N):
        ans = max(ans,dfs(i,j))
print(ans)
"""