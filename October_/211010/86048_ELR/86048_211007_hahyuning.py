from collections import defaultdict, deque


def solution(enter, leave):
    n = len(enter)
    stack = []
    cnt = defaultdict(list)
    leave = deque(leave)

    for x in enter:
        stack.append(x)

        for y in stack:
            if x != y:
                cnt[y].append(x)
                cnt[x].append(y)

        while leave and leave[0] in stack:
            y = leave.popleft()
            stack.remove(y)

    ans = []
    for i in range(1, n + 1):
        ans.append(len(set(cnt[i])))
    return ans