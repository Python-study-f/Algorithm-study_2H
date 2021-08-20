for i in range(10):
    a = int(input())
    array = []
    for _ in range(a):
        array.append(list(map(int, input().split())))
    count= 0
    for j in range(a):
        state = 0
        temp = 0
        for k in range(a):
            if array[k][j] == 1:
                state += 1
            if array[k][j] == 2 and state > 0:
                state = 0
                count += 1
    print("#{} {}".format(i+1, count))
                
            
