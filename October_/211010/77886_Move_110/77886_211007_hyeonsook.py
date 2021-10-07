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


# Stack
# https://programmers.co.kr/questions/17687
def solution(s):
    answer = []
    for seq in s:

        amount = 0
        while True:
            cnt = 0
            stack = []
            for char in seq:
                if char == "0" and stack[-2:] == ["1", "1"]:
                    cnt += 1

                    stack.pop()
                    stack.pop()
                else:
                    stack.append(char)
            seq = stack
            amount += cnt
            if cnt == 0:
                break

        result = "".join(seq)
        idx = result.rfind("0") + 1
        result = result[:idx] + "110" * amount + result[idx:]
        answer.append(result)
    return answer
