import bisect


def solution(n, t, m, timetable):
    idx, answer = 0, ""
    timetable = sorted(timetable)
    for i in range(n):
        hour, minute = divmod(540 + (i * t), 60)
        answer = f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"

        idx = bisect.bisect_right(timetable, answer)
        if i != n - 1:
            idx = min(idx, m)
            timetable = timetable[idx:]

    timetable = timetable[:idx]

    if len(timetable) >= m:
        hour, minute = map(int, timetable[m - 1].split(":"))
        hour, minute = divmod((hour * 60 + minute - 1), 60)
        answer = f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"

    return answer


print(
    solution(10, 60, 3, ["09:00", "09:00", "09:00", "09:00", "09:00", "09:00", "09:00"])
)
