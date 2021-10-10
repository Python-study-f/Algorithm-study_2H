# 한참 헤매다가 못풀음..
# 블로그 참조 https://chldkato.tistory.com/135


from collections import deque
import sys

def bfs(start):
    dq = deque()
    check = [False for _ in range(N)]
    dq.append(start[0])
    check[start[0]] = True

    cnt, ans = 1,0
    while dq:
        tmp = dq.popleft()
        ans += city[tmp]

        for t in data[tmp]:
            if t in start and not check[t]:
                check[t] = True
                cnt += 1
                dq.append(t)


    if cnt == len(start):
        return ans
    else:
        return False


def dfs(cnt, x, end):
    global _min

    # 원하는 구역의 개수만큼 도달했을 때
    if cnt == end:
        g1, g2 = deque(), deque()

        # 방문했으면 g1그룹으로 방문하지 않았으면 g2그룹으로 넣어준다
        for a in range(N):
            if visited[a]:
                g1.append(a)
            else:
                g2.append(a)

        # bfs를 통해 g1 deque안의 값이 인정한 값인지 확인
        ans1 = bfs(g1)

        # 아니라면 함수 바로 종료
        if not ans1:
            return

        # bfs를 통해 g2 deque안의 값이 인정한 값인지 확인
        ans2 = bfs(g2)

        # 아니라면 함수 바로 종료
        if not ans2:
            return

        # g1, g2둘다 인접한 구인지 확인이 되었다면 최소값 확인
        _min = min(_min, abs(ans1-ans2))
        return

    # 아직 end개수에 도달하지 못했을때는
    # for문을 통해 그 다음구역부터 새로운 구를 만들어준다.
    for a in range(x, N):
        # 방문을 했다면 무시
        if visited[a]:
            continue

        # 방문을 안했다면 visited 배열 바꿔주고 dfs탐색 시작
        visited[a] = True
        dfs(cnt+1, a, end)

        # back tracking
        visited[a] = False




N = int(input())
city = list(map(int,input().split()))

data = [[] for _ in range(N)]
_min = int(1e9)

for i in range(N):
    lst = list(map(int,input().split()))

    for j in lst[1:]:
        data[i].append(j-1)

for i in range(1, N//2 +1): # 예를 들어, N = 5일때 2,3 나누는 경우와 3,2 나누는 경우가 같기 때문에 N//2까지만 체크
    visited = [False for _ in range(N)]
    # 구역 찾기
    dfs(0,0,i)

if _min == int(1e9):
    print(-1)
else:
    print(_min)