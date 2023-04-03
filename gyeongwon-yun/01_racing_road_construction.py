from collections import deque

def solution(board):
    N = len(board)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # print(board)
    
    costs = [[[500*(N**2)]*4 for _ in range(N)] for _ in range(N)]
    costs[0][0] = [0]*4
    queue = deque([])

    if board[0][1] == 0:
        queue.append((0, 1, 1, 100))
    
    if board[1][0] == 0:
        queue.append((1, 0, 0, 100))
        
    while queue:
        cr, cc, d, cost = queue.popleft()
        # print(cr, cc, d, cost)

        if costs[cr][cc][d] < cost: # visited before and previous route is cheaper
            continue  
        if min(costs[cr][cc]) + 500 < cost: #previous route is cheaper even if corner is added
            continue      

        else:
            costs[cr][cc][d] = cost
            for i, (dr, dc) in enumerate(directions):
                if i == (d+2)%4: # opposite direction
                    continue
                if 0 <= cr+dr < N and 0 <= cc+dc < N and board[cr+dr][cc+dc] == 0:
                    if i == d:
                        queue.append((cr+dr, cc+dc, i, cost+100))
                    else:
                        queue.append((cr+dr, cc+dc, i, cost+600))

    # print(*costs, sep='\n')
    return min(costs[-1][-1])

def test(board):
    print(solution(board))

test([[0,0,0],[0,0,0],[0,0,0]])
test([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
