# LCA 알고리즘

import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())
    lst = [0 for _ in range(N+1)]

    for _ in range(N-1):
        parent, child = map(int,input().split())
        lst[child] = parent # 부모노드 저장

    A,B = map(int,input().split())
    parent_A = [A]
    parent_B = [B]

    # 각 노드의 부모노드가 루트일떄까지 모두 저장
    while lst[A]:
        parent_A.append(lst[A])
        A = lst[A]

    while lst[B]:
        parent_B.append(lst[B])
        B = lst[B]

    level_A = len(parent_A) - 1
    level_B = len(parent_B) - 1

    while parent_A[level_A] == parent_B[level_B]: # 부모노드가 같지 않을때까지
        level_A -= 1
        level_B -= 1

    print(parent_A[level_A+1])