from itertools import combinations
from copy import deepcopy
import sys

input = sys.stdin.readline

N,M,D = map(int,input().split())
enemys = set()

for a in range(N):
    lst = list(map(int,input().split()))

    for b in range(M):
        if lst[b] == 1:
            enemys.add((a,b)) # 적군들 좌표 저장

data = [[0 for _ in range(M)] for _ in range(N)]
archor_position = [(N,i) for i in range(M)] #궁수가 있을 수 있는 위치

comb = combinations(archor_position,3) # 궁수들 위치 3개를 고를 수 있는 모든 경우의 수

#궁수 위치별로 사격 가능한 적군 거리를 계산하는 함수
def get_distance(candidate):
    global D
    ableAttackArea = []

    for pos in candidate:
        px,py = pos
        copy = []

        for i in range(len(data)):
            for j in range(len(data[0])):
                if abs(px-i) + abs(py-j) <= D:
                    copy.append((abs(px-i) + abs(py-j),i,j))
        ableAttackArea.append(copy)

    return ableAttackArea

# 적군이 전진하는 함수
def move():
    global N
    return set([(i+1,j) for i,j in enemys if i + 1 < N])

# 공격 가능한 가장 가까운 적을 찾는 함수 ㄱx값이 작은 순서로 공격 가능한 위치 정렬
# 그 후, x,y축이 적군의 자표값이면, 좌표값 리턴
def findNearestEnemy(arc):
    arc.sort(key = lambda x: (x[0],x[2]))

    for dist, i, j in arc:
        if (i,j) in enemys:
            return i, j
    return None

_max = 0

for chance in comb:
    arc = get_distance(chance)
    kills = 0

    copyData = deepcopy(enemys)

    while enemys:
        tmp = set()

        for arc_map in arc:
            kill = findNearestEnemy(arc_map)
            if kill is not None:
                tmp.add(kill)
        kills += len(tmp)
        enemys -= tmp
        enemys = move()

    enemys = copyData
    _max = max(_max,kills)

print(_max)