def solution(places):
    answer = []
    visit = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    def dfs(pidx, x, y, cnt):
        if cnt >= 2:
            return True
        ans = True
        for d in range(4):
            tx, ty = x + dx[d], y + dy[d]
            if 0 <= tx < 5 and 0 <= ty < 5 and not visit[tx][ty]:
                visit[tx][ty] = True 
                if places[pidx][tx][ty] == 'P':
                    return False
                elif places[pidx][tx][ty] == 'O':
                    ans = ans and dfs(pidx, tx, ty, cnt + 1)
        return ans
                
        
        
    for p in range(len(places)):
        chk = True
        for i in range(5):
            for j in range(5):
                if places[p][i][j] == 'P':
                    visit = [[False]*5 for _ in range(5)]
                    visit[i][j] = True
                    if not dfs(p, i, j, 0):
                        chk =False
                        break
                
            if not chk:
                break
        if chk:
            answer.append(1)
        else:
            answer.append(0)
                

    
    return answer
