for _ in range(10):
       
    visited = [False]*100
    q = [0]

    a, b = map(int, input().split())

    graph = [[] for _ in range(100)]
    tmp = list(map(int, input().split()))

    for i in range(b):
        start = tmp[i*2]
        end = tmp[i*2+1]
        graph[start].append(end)

    while q:  
        now = q.pop() 

        if not visited[now]: 
            visited[now] = True  

            for i in graph[now]:
                if not visited[i]:
                    q.append(i)
    if visited[99]: result=1
    else: 0

    print("#{} {}".format(a, result))