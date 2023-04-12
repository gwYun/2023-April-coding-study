import sys
from copy import deepcopy

def solution(board):
    ones = 0

    for r in range(10):
        for c in range(10):
            if board[r][c] == 1:
                ones += 1

    global cnt
    cnt = 26
 
    
    dfs(board, 0, 0, 0, 0, 0, 0, ones, 5)

    return cnt if cnt > 0 else -1


        
        
        

def dfs(board, a, b, c, d, e, used, ones, limit):
    global cnt

    if ones == 0:
        cnt = min(cnt, used)
        return
    
    if used >= cnt:
        return
    
    if limit > 4 and e < 5 and ones >= 5**2:
        j = 5
        for r in range(10):
            for c in range(10):
                if board[r][c] == 1 and can_paste_chip(board, j, r, c):
                    new_board = deepcopy(board)
                    for x in range(r, r+j):
                        for y in range(c, c+j):
                            new_board[x][y] = 0
                    dfs(new_board, a, b, c, d, e+1, used+1, ones-j**2, j if e < 5 else j-1)
    
    if limit > 3 and d < 5 and ones >= 4**2:
        j = 4
        for r in range(10):
            for c in range(10):
                if board[r][c] == 1 and can_paste_chip(board, j, r, c):
                    new_board = deepcopy(board)
                    for x in range(r, r+j):
                        for y in range(c, c+j):
                            new_board[x][y] = 0
                    dfs(new_board, a, b, c, d+1, e, used+1, ones-j**2, j if d < 5 else j-1)
    if ones > sum(5*x**2 for x in [1, 2, 3]):
        return
    
    if limit > 2 and b < 5 and ones >= 3**2:
        j = 3
        for r in range(10):
            for c in range(10):
                if board[r][c] == 1 and can_paste_chip(board, j, r, c):
                    new_board = deepcopy(board)
                    for x in range(r, r+j):
                        for y in range(c, c+j):
                            new_board[x][y] = 0
                    dfs(new_board, a, b, c+1, d, e, used+1, ones-j**2, j if c < 5 else j-1)
    if ones > sum(5*x**2 for x in [1, 2]):
        return
    
    if limit > 1 and b < 5 and ones >= 2**2:
        j = 2
        for r in range(10):
            for c in range(10):
                if board[r][c] == 1 and can_paste_chip(board, j, r, c):
                    new_board = deepcopy(board)
                    for x in range(r, r+j):
                        for y in range(c, c+j):
                            new_board[x][y] = 0
                    dfs(new_board, a, b+1, c, d, e, used+1, ones-j**2, j if b < 5 else j-1)
    if ones > 5:
        return
    
    if limit > 0 and a < 5 and ones >= 1**2:
        j = 1
        for r in range(10):
            for c in range(10):
                if board[r][c] == 1 and can_paste_chip(board, j, r, c):
                    new_board = deepcopy(board)
                    for x in range(r, r+j):
                        for y in range(c, c+j):
                            new_board[x][y] = 0
                    dfs(new_board, a+1, b, c, d, e, used+1, ones-j**2, j if a < 5 else j-1)
    

def can_paste_chip(board, j, r, c):
    if r+j > 10 or c+j > 10: # out of board
        return False
    
    cropped_board = [row[c:c+j] for row in board[r:r+j]]

    multiply = 1
    for row in cropped_board:
        for x in row:
            multiply *= x
    
    if multiply == 1:
        return True
    
    return False

input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(10)]

# print(*board, sep='\n')
print(solution(board))

#반례: 5
'''
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
'''