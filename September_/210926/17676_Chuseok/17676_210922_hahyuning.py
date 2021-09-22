def solution(lines):
    logs = []

    # 시간 밀리초로 변환
    for x in lines:
        date, e, t = x.split(" ")
        h, m, s = e.split(":")
        e = (int(h) * 3600 + int(m) * 60 + float(s)) * 1000
        s = e - float(t[:-1]) * 1000 + 1

        logs.append((s, e))

    ans = 1
    for i in range(len(logs) - 1):
        cnt = 1
        for j in range(i + 1, len(logs)):

            # 끝나는 시간이 3초 보다 크게 차이나면 겹치는 부분 x
            if logs[j][1] - logs[i][1] >= 4000:
                break

            # 1초 이내에 겹치는 부분이 존재하는 경우
            if logs[j][0] - logs[i][1] < 1000:
                cnt += 1

        ans = max(ans, cnt)

    return ans