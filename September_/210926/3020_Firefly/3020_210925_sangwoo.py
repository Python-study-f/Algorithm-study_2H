n,h = map(int, input().split())
top = []
down = []
for i in range(n):
    temp = int(input())
    if i % 2 == 0:
        down.append(temp)
    else:
        top.append(h - temp)
carray = []
for j in range(1, h+1):
    dcount = 0
    ucount = 0
    for a in down:
        if j <= a:
            dcount += 1
    for b in top:
        if j > b:
            ucount += 1
    tcount = dcount + ucount
    carray.append(tcount)

print(min(carray), carray.count(min(carray)))

