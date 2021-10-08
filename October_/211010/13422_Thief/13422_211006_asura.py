from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N,M,K = map(int,input().split())
    data = list(map(int,input().split()))
    data.extend(data) # 원형만들기

    if N == M: # N과 M이 같으면 모든 총합이 같음. 예를들어 1,3,5 이고
        check = 0
        for i in range(N):
            check += data[i]

        if check < K:
            print("1")
            continue

    cnt, check = 0, 0

    for i in range(N):
        if i == 0:
            check = sum(data[0:M])

        else:
            check = check - data[i-1] + data[i-1+M]

        if check < K:
            cnt += 1

    print(cnt)

# TLE 그냥 한번 풀어봤음
# T = int(input())
#
# for tc in range(T):
#     N,M,K = map(int,input().split())
#     data = list(map(int,input().split()))
#     data.extend(data) # 원형 큐 만들기
#     lst = []
#     cnt = 0
#
#     for i in range(N):
#         check = sum(data[i:i+M])
#         lst.append(check)
#
#     for i in lst:
#         if i < K:
#             cnt += 1
#     print(cnt)

