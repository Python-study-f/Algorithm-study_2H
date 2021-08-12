from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 1. 가장 가까운 승객 찾기 -> 승객의 좌표와 거리 리턴
def find_guest(sx, sy):
    # 예외처리: 택시가 있는 위치에 손님이 있는 경우
    if (sx, sy) in guest:
        return (sx, sy, 0)

    q = deque()
    q.append((sx, sy))
    check = [[-1] * n for _ in range(n)]
    check[sx][sy] = 0
    # 택시가 있는 위치부터 모든 승객의 좌표와 거리
    res = []

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == -1 and a[nx][ny] != 1:
                if (nx, ny) in guest:
                    res.append((nx, ny, check[x][y] + 1))
                q.append((nx, ny))
                check[nx][ny] = check[x][y] + 1
    # 예외처리: 태울 수 있는 승객이 없는 경우
    if not res:
        return (-1, -1, -1)
    else:
        res.sort(key=lambda x:(x[2], x[0], x[1]))
        return (res[0][0], res[0][1], res[0][2])

# 2. 목적지부터 출발지까지의 거리 구하기 -> 거리 반환
def guest_move(sx, sy):
    q = deque()
    q.append((sx, sy))
    check = [[-1] * n for _ in range(n)]
    check[sx][sy] = 0

    ex, ey = guest[(sx, sy)]

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == -1 and a[nx][ny] != 1:
                if (nx, ny) == (ex, ey):
                    return check[x][y] + 1
                else:
                    q.append((nx, ny))
                    check[nx][ny] = check[x][y] + 1

    # 예외처리: 승객이 목적지까지 갈 수 없는 경우
    return -1

n, m, fuel = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
# 택시의 현재 위치
sx, sy = map(int, input().split())
sx -= 1
sy -= 1
# 승객 정보 (출발지:목적지 형태)
guest = dict()
for _ in range(m):
    x, y, w, z = map(int, input().split())
    x -= 1
    y -= 1
    w -= 1
    z -= 1
    guest[(x, y)] = (w, z)

flg = True
while True:
    gx, gy, d = find_guest(sx, sy)
    # 아직 승객이 남았지만 택시가 승객에게 갈 수 없는 경우
    if d == -1:
        if len(guest.keys()) != 0:
            flg = False
        break

    # 택시가 승객을 태우러 갈 수 있는 경우
    if d <= fuel:
        fuel -= d
        use = guest_move(gx, gy)
        # 승객이 목적지까지 도달할 수 없는 경우
        if use == -1:
            flg = False
            break

        if use <= fuel:
            fuel += use
            # 택시의 위치 갱신
            sx, sy = guest[(gx, gy)]
            # 승객 목록에서 제거
            del guest[(gx, gy)]
        # 목적지까지 가는데 연료가 부족한 경우
        else:
            flg = False
            break
    # 승객을 태우러 가는데 연료가 부족한 경우
    else:
        flg = False
        break

print(fuel if flg else -1)
