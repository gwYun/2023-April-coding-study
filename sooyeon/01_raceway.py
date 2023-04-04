'''
2020 카카오 인턴십 - . 경주로 건설
https://school.programmers.co.kr/learn/courses/30/lessons/67259
'''
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def solution(board):
    n = len(board)
    dq = deque()
    vis = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]

    dq.append((0, 0, -1))  # x, y, dir
    for i in range(4):
        vis[0][0][i] = 0  # money

    while dq:
        x, y, prev_dir = dq.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 1:
                continue

            if (x == 0 and y == 0):
                prev_dir = dirß

            if prev_dir == dir:
                nx_money = vis[x][y][prev_dir] + 100
            else:
                nx_money = vis[x][y][prev_dir] + 600

            if vis[nx][ny][dir] > nx_money:
                dq.append((nx, ny, dir))
                vis[nx][ny][dir] = nx_money

    return min(vis[n - 1][n - 1])


if __name__ == '__main__':
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(solution(board))

    board = [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
    print(solution(board))

    board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
    print(solution(board))

    board = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0]]
    print(solution(board))
