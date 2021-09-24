def solution(lines):
    answer = 0
    arr = []

    def cal(time):
        num = (int(time[0:2]) * 3600 + int(time[3:5]) * 60) * 1000
        sec = float(time[6:]) * 1000.0
        num += int(sec)
        return num

    mn, mx = 24*3600*1000, 0
    
    for line in lines:
        temp = line.split()
        end = cal(temp[1])
        start = cal(temp[1]) - int(float(temp[2][:-1])*1000.0 - 1) - 999
        arr.append([start, end])
        mn = min(mn, start)
        mx = max(mx, end)

    record = [0]*(mx-mn+1)  # 1초 영향권에 있는 로그들

    for a in arr:
        for t in range(a[0], a[1]+1):
            record[t-mn] += 1

    return max(record)
