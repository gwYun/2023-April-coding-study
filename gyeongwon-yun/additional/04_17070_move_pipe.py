import sys
from collections import deque

def solution(N, board):
    directions = {'rr': (0, 1), 'rd': (1, 1), 'dd': (1, 0)}
    
    cases = 0
    queue = deque([(0, 1, 'rr')])
    while queue:
        cr, cc, cd = queue.popleft()

        if cr == N-1 and cc == N-1:
            cases += 1
            continue
        
        else:
            if cd != 'rr':
                dr, dc = (1, 0)
                if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != 1:
                    queue.append((nr, nc, nd))
            
            if cd != 'dd':
                dr, dc = (0, 1)
                if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != 1:
                    queue.append((nr, nc, nd))

            for nd in ['rr', 'rd', 'dd']:
                dr, dc = directions[nd]
                nr = cr+dr
                nc = cc+dc

                if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != 1:
                    if nd == 'rd' and (board[nr][nc-1] == 1 or board[nr-1][nc] == 1):
                        continue
                    queue.append((nr, nc, nd))
                        
    return cases

input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for i in range(N)]

# print(N, *board, sep='\n')
print(solution(N, board))