from collections import deque

def solution(board, moves):
    board = list(map(deque, zip(*board)))
    for c in board:
        while len(c)>0 and c[0] == 0:
            c.popleft()
    # print(*board, sep='\n')
    basket = []
    answer = 0
    while len(moves) > 0:
        m = moves.pop(0)-1
        if board[m]:
            doll = board[m].popleft()
            
            if len(basket)>0 and basket[-1] == doll:
                basket.pop()
                answer += 2

            else:
                basket.append(doll)
    return answer