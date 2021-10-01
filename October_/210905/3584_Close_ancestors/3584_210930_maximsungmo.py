import sys

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())

    graph = [0 for _ in range(N + 1)]
    for _ in range(N - 1):
        parent, child = map(int, input().split())
        graph[child] = parent

    goals = list(map(int, input().split()))

    first_node_parents = []
    # 1번 목표물의 모든 조상을 구한다.
    parent_target = goals[0]
    for _ in range(N):
        first_node_parents.append(parent_target)
        parent_target = graph[parent_target]
        if parent_target == 0:
            break


    # 2번 목표물의 조상을 구하며 1번 목표물의 조상과 겹치면 멈춘다.
    parent_target = goals[1]
    for _ in range(N):
        if parent_target in first_node_parents:
            print(parent_target)
            break
        parent_target = graph[parent_target]


