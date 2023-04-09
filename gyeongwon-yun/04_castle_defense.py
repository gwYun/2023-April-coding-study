# https://www.acmicpc.net/problem/17135

import sys
from copy import deepcopy
input = sys.stdin.readline

def solution(N, M, D, board):
    board.reverse()
    max_kills = 0
    for i in range(M-2):
        for j in range(i+1, M-1):
            for k in range(j+1, M):
                initial_board = deepcopy(board)
                
                kills = 0
                for rounds in range(N):
                    # print('round:', rounds)
                    # print(*list(reversed(initial_board)), "", sep='\n')
                    kills += kill(i, j, k, N, M, D, initial_board)
                    initial_board.pop(0)
                    initial_board.append([0]*M)
                
                max_kills = max(max_kills, kills)

    return max_kills

def kill(a1, a2, a3, N, M, D, board):
    kills = set()
    for pos_archer in [a1, a2, a3]:
        killed = False
        for distance in range(D):
            r_0, c_0 = 0, pos_archer
            for dc in range(-distance, distance+1):
                dr = distance - abs(dc)
                if 0 <= r_0 + dr < N and 0 <= c_0 + dc < M and board[r_0 + dr][c_0 + dc] == 1:
                    # print('killed:', (r_0 + dr, c_0 + dc))
                    killed = True
                    kills.add((r_0 + dr, c_0 + dc))
                    break
            if killed:
                break
    for kr, kc in kills:
        board[kr][kc] = 0
    # print(*list(reversed(board)), "", sep='\n')

    
    return len(kills)
    

N, M, D = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]

# print(N, M, D, *board, sep = '\n')
print(solution(N, M, D, board))
