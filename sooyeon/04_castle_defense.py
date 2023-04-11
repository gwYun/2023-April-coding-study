'''
https://www.acmicpc.net/problem/17135
'''
import sys

sys.stdin = open('../input.txt', 'r')

from itertools import combinations
from collections import deque
from copy import deepcopy


def print_board(board):
    for i in range(N):
        print(*board[i])
    print()


def kill_enemy(board, targets):
    for tr, tc in targets:
        board[tr][tc] = 0
    return len(targets)


def move_enemy(board):
    board.pop()
    board.appendleft([0] * M)


def end_game(board):
    return False if sum(sum(board[i]) for i in range(N)) else True


ans = -1

N, M, D = map(int, input().split())
board = deque([deque(map(int, input().split())) for _ in range(N)])

combis = combinations(range(M), 3)
for archers in combis:
    tmp_board = deepcopy(board)
    n_kill = 0
    while True:
        targets = set()
        for archer in archers:
            r, c = N, archer
            set_target = False
            for d in range(1, D + 1):
                for i in range(2 * d - 1):
                    if i == 0:
                        nr, nc = r - 1, c - (d - 1)
                    elif i < d:
                        nr, nc = nr - 1, nc + 1
                    else:
                        nr, nc = nr + 1, nc + 1

                    if nr < 0 or nr >= N or nc < 0 or nc >= M:
                        continue

                    if tmp_board[nr][nc] == 1:
                        targets.add((nr, nc))
                        set_target = True
                        break
                if set_target:
                    break
        n_kill += kill_enemy(tmp_board, targets)
        move_enemy(tmp_board)

        if end_game(tmp_board):
            ans = max(ans, n_kill)
            break

print(ans)
