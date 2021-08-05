a = int(input())
b = [0]
maxx = [0]*(a+1)

for k in range(a):
    b.append(int(input()))
    
for i in range(1, a + 1):
    if i == 1:
        maxx[1] =  b[1]
    elif i == 2:
        maxx[2] = b[1] + b[2]
    else:
        x = b[i] + b[i-1] + maxx[i-3]
        y = b[i] + maxx[i-2]
        z = maxx[i-1]
        maxx[i] = max(x, y, z)

print(maxx[i])
