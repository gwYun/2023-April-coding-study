import sys
from itertools import permutations
from copy import deepcopy

def solution(N, M, K, board, operations):
    global min_val
    min_val = sum([sum(row) for row in board])

    perms = list(permutations(range(K), K))
    # print(perms)
    for operation_order in perms:
        new_board = deepcopy(board)
        for o in operation_order:
            r, c, size = operations[o]
            rotate(new_board, r-1, c-1, size)
            # print('after rotation:', *new_board, sep='\n')
        min_val = min(min_val, min([sum(row) for row in new_board]))
            
    return min_val

def rotate(board, r, c, size):
    for i in range(1, size+1):
        start = board[r-i][c-i]
        for j in range(2*i):
            board[r-i+j][c-i] = board[r-i+j+1][c-i]
        for j in range(2*i):
            board[r+i][c-i+j] = board[r+i][c-i+j+1]
        for j in range(2*i):
            board[r+i-j][c+i] = board[r+i-j-1][c+i]
        for j in range(2*i-1):
            board[r-i][c+i-j] = board[r-i][c+i-j-1]
        board[r-i][c-i+1] = start


input = sys.stdin.readline

N, M, K = list(map(int, input().split(' ')))
board = [list(map(int, input().split(' '))) for _ in range (N)]
operations = [list(map(int, input().split(' '))) for _ in range(K)]

# print(N, M, K, *board, *operations, sep='\n')
print(solution(N, M, K, board, operations))
