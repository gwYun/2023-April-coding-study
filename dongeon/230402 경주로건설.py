from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def bfs(x,y,direction,cost,board):
    n = len(board)
    q = deque()
    q.append((x,y,direction,cost))
    INF = int(1e9)
    visited = [[[INF] * n for _ in range(n)] for _ in range(4)] 
    
    while q:        
        x,y,direction,cost = q.popleft()        
        
        if x == n-1 and y == n-1: # 도착지점에 도달하면 패스
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0: # 도로이거나 범위 안일경우
                if direction == -1: #시작점인 경우
                    new_cost = cost + 100
                elif direction % 2 == i % 2: #직진
                    new_cost = cost + 100
                else:
                    new_cost = cost + 600 #코너
                        
                if new_cost < visited[i][nx][ny]:
                    q.append((nx,ny,i,new_cost))
                    visited[i][nx][ny] = new_cost
    minVal = INF
    
    for i in range(4):
        minVal = min(minVal, visited[i][-1][-1])
    return minVal

def solution(board):

    return bfs(0,0,-1,0,board)
        
    