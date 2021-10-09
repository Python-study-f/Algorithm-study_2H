from collections import deque
def solution(s):
    answer = []
    for word in s:
        array = []
        count = 0
        for w in word:
            if w == '0':
                if array[-2:] == ['1', '1']:
                    count += 1
                    array.pop()
                    array.pop()
                else:
                    array.append(w)
            else:
                array.append(w)
        if count == 0:
            answer.append(word)
        else:
            state = True
            temp = 0
            tarray = deque()
            for i in array:
                if i == '1':
                    if state == True:
                        temp += 1
                    tarray.append(i)
                else:
                    if state == True:
                        temp = 0
                    tarray.append(i)
                if temp == 3:
                    tarray.pop()
                    tarray.pop()
                    tarray.pop()
                    for _ in range(count):
                        tarray.append("1")
                        tarray.append("1")
                        tarray.append("0")
                    tarray.append("1")
                    tarray.append("1")
                    tarray.append("1")
                    state = False
            if state == True:
                for _ in range(count):
                    tarray.append("1")
                    tarray.append("1")
                    tarray.append("0")
            answer.append(''.join(map(str,tarray)))
                            
    return answer
