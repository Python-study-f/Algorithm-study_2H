from collections import deque

for _ in range(10):
    a, b = map(int, input().split())
    array = list(map(int, input().split()))
    dic = {}
    for i in range(0, b*2, 2):
        if array[i] in dic:
            dic[array[i]].append(array[i+1])
        else:
            dic[array[i]] = [array[i+1]]
    q = deque()
    q.append(0)
    visit = [0] * 100
    while q:
        a = q.pop()
        visit[a] = 1
        if a in dic.keys():
            for k in dic[a]:
                if not visit[k]:
                    q.append(k)
    print('#{} {}'.format(a, visit[-1]))
    
    



