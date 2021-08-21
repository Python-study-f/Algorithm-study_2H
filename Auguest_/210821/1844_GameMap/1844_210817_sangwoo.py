from collections import deque

def solution(maps):
    q = deque()
    
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    n = len(maps)
    m = len(maps[0])    
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < n and 0 <= ty < m and maps[tx][ty] == 1:
                q.append((tx, ty))
                maps[tx][ty] = maps[x][y] + 1
    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]
