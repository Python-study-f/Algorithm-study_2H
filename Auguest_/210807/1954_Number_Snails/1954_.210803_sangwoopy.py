a = int(input())
b = []

for j in range(a):
    b.append(int(input()))
for i in range(len(b)):
    array = [[0 for col in range(b[i])] for row in range(b[i])]
    direction = 'right'
    x = 0
    y = 0
    for k in range(1, b[i] * b[i] + 1):
        if direction == 'right':    
            array[x][y] = k
            y += 1
            if y == b[i] or array[x][y] != 0:
                x += 1
                y -= 1
                direction = 'down'
        elif direction == 'down': 
            array[x][y] = k
            x += 1
            if x == b[i] or array[x][y] != 0:
                x -= 1
                y -= 1
                direction = 'left'
        elif direction == 'left':
            array[x][y] = k
            y -= 1
            if y < 0 or array[x][y] != 0:
                x -= 1
                y += 1
                direction = 'up'
        elif direction == 'up':
            array[x][y] = k
            x -= 1
            if x < 0 or array[x][y] != 0:
                x += 1
                y += 1
                direction = 'right'
        else:
            print("error")
    print("#{}".format(i+1))
    for t in range(b[i]):
        for e in range(b[i]):
            print(array[t][e], end=" ")
        print()

    
    
