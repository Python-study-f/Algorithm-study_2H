from sys import stdin
input = stdin.readline

a = int(input())
for _ in range(a):
    b = int(input())
    parent = [0] * (n + 1)
    for _ in range(n - 1):
        c ,d = map(int, input().split())
        parent[d] = c
    c, d = map(int, input().split())
    array = []
    while parent[c] != c:
        array.add(c)
        c = parent[c]

    while d not in result:
        d = parent[d]
    print(d)
    

    
