# 효율성 실패

from collections import deque

def solution(n, k, cmds):
    k+=1
    temp = []
    for cmd in cmds:
        if cmd[0] == 'U':
            for _ in range(int(cmd[2])):
                k -= 1
                while k in temp:
                    k -= 1
                    
        elif cmd[0] == 'D':
            for _ in range(int(cmd[2])):
                k += 1
                while k in temp:
                    k += 1
                    
        elif cmd[0] == 'C':
            temp.append(k)
            if k == n:
                k -= 1
            else:
                k += 1
            
        elif cmd[0] == 'Z':
            a = temp.pop()
           
    answer = ""
    for j in range(1, n+1):
        if j in temp:
            answer += "X"
        else:
            answer += "O"
    print(answer)

solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
