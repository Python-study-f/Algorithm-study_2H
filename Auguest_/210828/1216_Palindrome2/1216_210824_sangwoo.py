def check(array):
    answer = 1
    for i in range(100):
        for j in range(100):
            for k in range(j, 100):
                word = array[i][j:k]
                if word == word[::-1]:
                    if len(word) > answer:
                        answer = len(word)
    return answer

for _ in range(10):
    a = int(input())
    array = []
    for _ in range(100):
        array.append(input())
    row = check(array)
    
    new_array = []
    for i in range(100):
        temp = ''
        for j in range(100):
            temp += array[j][i]
        new_array.append(temp)

    col = check(new_array)
    print("#{} {}".format(a, max(row, col)))
        
        
