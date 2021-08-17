from collections import deque
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def check(place,x,y):
    visited = [[0]*5 for _ in range(5)]
    q=deque()
    q.append([x,y,0])
    visited[x][y] = 1

    while q:
        now=q.popleft()
        if place[now[0]][now[1]] == "P" and 0<now[2]<=2:
            return False
        if now[2]>=3:
            break
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            cnt=now[2]+1
            
            if 0 <=nx<5 and 0<=ny<5:
                if place[nx][ny]!='X' and visited[nx][ny]==0:
                    q.append((nx,ny,cnt))
                    visited[nx][ny]=1
            
def solution(places):
    answer = []
    for place in places:
        Flag=True
        for x in range(len(place)):
            for y in range(len(place[0])):
                if place[x][y] == "P":
                    if check(place,x,y)==False:
                        Flag=False
                        break
        if Flag==False:
            answer.append(0)
        else:
            answer.append(1)

    return answer