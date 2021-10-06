# 81.0 시간 초과 -> 59.9
def solution(s):
    answer = []
    for str in s:
        cnt = 0
        strs = str.strip()
        while True:
            tmp = strs.strip().split("110")

            if len(tmp) == 1:
                break

            cnt += len(tmp) - 1
            strs = "".join(tmp)

        idx = strs.rfind("0") + 1
        strs = strs[:idx] + "110" * cnt + strs[idx:]
        answer.append(strs)
    return answer
