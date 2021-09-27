import sys

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())

    graph = [0 for _ in range(N + 1)]
    for _ in range(N - 1):
        p, c = map(int, input().split())
        graph[c] = p

    goals = list(map(int, input().split()))

    path = {goal: [goal] for goal in goals}
    for goal in goals:
        p = goal
        while p > 0:
            p = graph[p]
            path[goal].append(p)

    stack1 = path[goals[0]]
    stack2 = path[goals[1]]
    answer = -1
    while stack1 and stack2:
        if stack1[-1] == stack2[-1]:
            answer = stack1[-1]
            stack1.pop()
            stack2.pop()
        else:
            break

    print(answer)
