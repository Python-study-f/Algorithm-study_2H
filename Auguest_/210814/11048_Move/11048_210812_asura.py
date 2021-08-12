# 1. N,M 범위를 보니 dfs는 좀 힘들어 보임
# 2. dfs말고 bfs로 해결


# 풀이1. bfs
"""
from collections import deque

N,M = map(int,input().split())
dx = [1,0,1] # R,D,C
dy = [0,1,1]
max_kkakka=0

data = [list(map(int,input().split())) for _ in range(N)]
visited = [[-1]* M for _ in range(N)]

def bfs():
    dq = deque()
    dq.append((0,0))    # 시작점

    visited[0][0] = data[0][0] # candy 데이터 추가

    while dq:
        x,y = dq.popleft()

        for i in range(3):
            nx,ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M: # 범위안에 든다면,
                tot = visited[x][y] + data[nx][ny] # total 이전의 값 + 이동할 방향의 data값

                if visited[nx][ny] < tot: # tot의 값이 다음 이동할 값보다 크다면,
                    visited[nx][ny] = tot
                    dq.append((nx,ny))
    return visited[-1][-1]

print(bfs())
"""

#풀이2. DP
N,M = map(int,input().split())
dp = [[0] * (M+1) for _ in range(N+1)]
data = []

for i in range(N):
    data.append(list(map(int,input().split())))

for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + data[i-1][j-1]

print(dp[-1][-1])
# 후기 : DP가 더 풀기 편하네요 ㅎㅎ... DP로 생각하신 분들은 왜 DP로 접근하셨나요!?