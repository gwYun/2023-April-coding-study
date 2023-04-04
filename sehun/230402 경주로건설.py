#BFS 탐색하되 코너값 계산위해 이전도로 방향과 일치확인후
#비일치(코너)일시 추가금액 증대해서 서칭

from collections import deque

def solution(board):
    n = len(board)
    cost = [[[(1e9) for _ in range(4)] for _ in range(n)] for _ in range(n)]

    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    
    #xy, 전방향, cost
    q = deque([(0, 0, 1, 0),(0, 0, 0, 0)]) 
    
    while q:
        x, y, direction, cur_cost = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            
            if 0<= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                #직선
                if direction == i:
                    ncost = cur_cost + 100
                #코너
                else:
                    ncost = cur_cost + 600
                if cost[nx][ny][i] > ncost:
                    cost[nx][ny][i] = ncost
                    q.append((nx, ny, i, ncost))
                
    answer = min(cost[n-1][n-1])
    return answer