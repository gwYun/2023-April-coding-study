# 2020 카카오 인턴십
# 경주로 건설
# https://heyksw.tistory.com/m/6
from collections import deque
from copy import deepcopy
dx,dy = (-1,0,1,0),(0,-1,0,1)
def bfs(x,y,cost,d):
    global N,board
    money = deepcopy(board)
    q=deque()
    q.append((x,y,cost,d))
    while q:
        x,y,cost,idx = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            
            if nx<0 or nx>=N or ny<0 or ny>=N or money[nx][ny]==1 : continue
            
            if idx==i : newcost=cost+100
            else:newcost=cost+600
            
            if money[nx][ny]==0 or money[nx][ny]>newcost:
                q.append((nx,ny,newcost,i))
                money[nx][ny]=newcost
            
    return money[N-1][N-1]

    


def solution(MAP):
    global N,board
    board = deepcopy(MAP)
    N=len(board)
    
    return min(bfs(0,0,0,2),bfs(0,0,0,3))



'''
from copy import deepcopy
from pprint import pprint

dx = (0,0,-1,1)
dy = (-1,1,0,0)
INF = int(1e9)  

def dfs(bx,by,x,y):
    global board,money,N,visited
    print(bx,by,x,y)
    #print(log)    
    #log2 = deepcopy(log)
    #log2.append((x,y))

    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if nx<0 or ny<0 or nx>=N or ny>=N or board[nx][ny]==1  or visited[nx][ny]==True: # or ((nx,ny) in log )
            continue
        
        if bx==nx or by==ny :  # x 또는 y 좌표가 같으면 직선도로, 그외는 코너! 
            total_cost = money[x][y] + 100
        else:
            total_cost = money[x][y]+ 600

        if total_cost <= money[nx][ny]+500:
            money[nx][ny] = total_cost
            visited[nx][ny]=True
            dfs(x,y,nx,ny)
            visited[nx][ny]=False

    
       
   
def solution(MAP):
    global N,money, board,visited
    board = deepcopy(MAP)
    N = len(board)
    money = [[INF]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    
    money[0][0]=0
    dfs(0,0,0,0)
    
    answer = money[N-1][N-1]
    pprint(money)
    print(answer)
    return answer

'''
solution([[0,0,0],[0,0,0],[0,0,0]])
solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])#3800
solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])	#2100
solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])#	3200