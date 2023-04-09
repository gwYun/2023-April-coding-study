def solution(board, moves):
    answer = 0
    N = len(board)
    columns = [[] for _ in range(N)]
    for i in range(N-1,-1,-1):
        for j in range(N):
            if board[i][j]!=0:
                columns[j].append(board[i][j])
                
    stack = []
    for move in moves:
        if columns[move-1]: # 뽑을 인형 있으면 
            new = columns[move-1].pop(-1)
            if stack and stack[-1]==new:
                stack.pop(-1)
                answer+=2
            else:
                stack.append(new)
    return answer