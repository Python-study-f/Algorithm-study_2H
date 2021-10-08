
# https://pythontutor.com/visualize.html#mode=display 시각화해서 보면 편한 것 같아요
# Stack 자료구조로 풀은 문제.
# 들어오고 나오는 것을 체크하고 남은 잔여 사람으로 count && 빠져나간사람까지 + 1

def solution(enter, leave):
    ans = [0] * len(enter)
    room = []
    enter_idx = 0

    for i in leave:
        while i not in room:
            room.append(enter[enter_idx])
            enter_idx += 1
        room.remove(i)

        for check in room:
            ans[check - 1] += 1
        ans[i - 1] += len(room)
    return ans