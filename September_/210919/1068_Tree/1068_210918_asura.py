import copy

def dfs(grap,visit,v): # dfs 방식 탐색
    global count
    visit[v] = True # 방문처리

    if len(grap[v]) == 0: # 리프노드일 경우 count += 1
        count += 1

    for i in grap[v]:
        if not visit[i]:
            dfs(grap,visit,i)
    return count

def remove(t_grap,grap,visit,v):
    visit[v] = True

    for i in range(N): # 그래프를 조회하며 dfs 방식으로 탐색한 노드들을 tempgraph에서 삭제
        for j in range(len(grap[i])):
            if grap[i][j] == v:
                t_grap[i].remove(v)

    for i in grap[v]:
        if not visit[i]:
            remove(t_grap,grap,visit,i)
#                                                       #
#                                                       #
N = int(input())
graph = [[] for _ in range(N+1)]
data = list(map(int,input().split()))
del_node = int(input())
root = -1


for a in range(N):
    if data[a] == -1: # 부모노드가 -1인 경우, 루트노드 설정
        root = a
        continue
    graph[data[a]].append(a) # 루트노드가 아니면 그래프 연결



if del_node != root: # 지우려고 하는 노드가 루트노드가 아니라면,
    temp = copy.deepcopy(graph)
    count = 0
    visited = [0] * (N+1)
    remove(temp,graph,visited,del_node)

    count = 0
    visited = [0] * (N+1)
    print(dfs(temp,visited,root))

else:
    print(0)
