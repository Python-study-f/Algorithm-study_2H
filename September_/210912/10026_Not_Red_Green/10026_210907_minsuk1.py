import sys
sys.setrecursionlimit(10000)

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n = int(input())
data = [list(input()) for _ in range(n)]
import copy
data2 = copy.deepcopy(data)  

def dfs(x,y,color):
    data[x][y] = '0'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n :
            if data[nx][ny] in color:
                 dfs(nx,ny,color)
                    
def dfs2(x,y,color):
    data2[x][y] = '0'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n :
            if data2[nx][ny] in color:
                 dfs2(nx,ny,color)
                    
                    
answer = [0,0]
for i in range(n):
    for j in range(n):
        if data[i][j] == 'R':
            answer[0]+=1
            dfs(i,j,['R'])
            
        if data[i][j] == 'G':
            answer[0]+=1
            dfs(i,j,['G'])
            
        if data[i][j] == 'B':
            answer[0]+=1
            dfs(i,j,['B'])

            
for i in range(n):
    for j in range(n):
        if data2[i][j] == 'R' or data2[i][j] == 'G':
            answer[1]+=1
            dfs2(i,j,['R','G'])
            
        if data2[i][j] == 'B':
            answer[1]+=1
            dfs2(i,j,['B'])
            
print(*answer)