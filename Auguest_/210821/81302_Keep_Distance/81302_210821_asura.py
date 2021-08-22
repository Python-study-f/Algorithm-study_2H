from collections import deque


def solution(places):
    result = []

    for place in places:
        board = [list(s) for s in place]  # 5x5로 칸으로 나누기
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1), (-2, 0), (2, 0), (0, 2), (0, -2), (1, -1), (1, 1), (-1, 1),
                (-1, -1)]  # 해밀턴 거리가 2이내인 방향

        targets = deque((x, y) for x in range(5) for y in range(5) if board[x][y] == "P")  # 모든 응시자 위치 찾기

        is_distancing = True  # 거리두기 지킴 여부
        while targets and is_distancing:  # 모든 응시자 대상 검사를 하되, 거리두기를 어긴 경우는 검사를 그만둔다.
            cx, cy = targets.popleft()

            for dx, dy in dirs:
                h_distance = abs(dx) + abs(dy)  # 해밀턴 거리 계산
                nx, ny = cx + dx, cy + dy
                if nx < 0 or nx >= 5 or ny < 0 or ny >= 5: continue  # 칸 예외처리
                if board[nx][ny] != "P": continue  # 검사하고자 하는 위치에 사람이 아닌 경우는 검사 제외

                if h_distance < 2:  # 해밀턴 거리가 2 보다 작은 경우는 예외 경우 X
                    is_distancing = False
                    break

                if dx != 0 and dy != 0:  # 대각선 방향으로 해밀턴 거리 2인 경우
                    if board[cx + dx][cy] != "X" or board[cx][cy + dy] != "X":  # 응시자 자리 사이가 파티션으로 막히지 않은 경우
                        is_distancing = False
                        break
                else:  # 상하좌우 방향으로 해밀턴 거리 2인 경우
                    chk_x, chk_y = cx + (dx // 2), cy + (dy // 2)
                    if board[chk_x][chk_y] != "X":  # 응시자 자리 사이가 파티션으로 막히지 않은 경우
                        is_distancing = False
                        break
        if is_distancing:
            result.append(1)
        else:
            result.append(0)

    return result