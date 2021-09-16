def print_time(t):
    return str(t // 60).zfill(2) + ":" + str(t % 60).zfill(2)

def solution(n, t, m, timetable):
    timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    timetable.sort()

    now = 540
    idx = 0
    cnt = 0
    for i in range(n):
        cnt = 0
        while True:
            # 종료조건
            # 1. 전체 승객을 모두 태운 경우
            if idx >= len(timetable):
                break
            # 2. 버스에 태운 승객이 m명인 경우
            if cnt == m:
                break
            # 3. 버스 출발 시간보다 늦게 온 경우
            if timetable[idx] > now:
                break
            cnt += 1
            idx += 1
        now += t

    # 마지막 셔틀에 탑승하는 승객이 m명일 경우
    # 마지막 사람보다 1분 전에 도착
    if cnt == m:
        return print_time(timetable[idx - 1] - 1)
    # 마지막 셔틀에 탑승하는 승객이 m명 미만인 경우
    # 마지막 셔틀 시간에 도착
    return print_time(now - t)
