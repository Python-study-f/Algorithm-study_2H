# LCA Algorithm 응용

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    depth = [0]*(N+1)
    parent = [0]*(N+1)
    for _ in range(N-1):
        f, c = map(int, input().split())
        parent[c] = f

    x, y = map(int, input().split())

    x_parent = [x]
    y_parent = [y]

    while parent[x]:
        x_parent.append(parent[x])
        x = parent[x]
    while parent[y]:
        y_parent.append(parent[y])
        y = parent[y]
        
    x_level = len(x_parent) - 1
    y_level = len(y_parent) - 1
    
    # 루트노드부터 차례대로 비교, 마지막이 루트노드
    while x_parent[x_level] == y_parent[y_level]:  
        x_level -= 1
        y_level -= 1

    print(x_parent[x_level + 1])
