import sys

input = sys.stdin.readline
# 색종이를 순회하면서 1을 만나면 1~5 중에 덮어지는 색종이를 dfs 탐색한다.
# 색종이 개수가 0이면 continue
# 최소 개수 출력
board = []

for _ in range(10):
    board.append(list(map(int, input().split())))

paper = [5] * 5

ans = 101

def check_paper(x, y, board, size): # 색종이를 덮을수 있는지 확인하는 함수
    for i in range(x, x + size + 1):
        for j in range(y, y + size + 1):
            if board[i][j] == 0:
                return False
    return True


def check_empty(board):# 1을 다 덮었는지 확인하는 함수
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                return False
    return True


def dfs(x, y, cnt):
    
    global ans
    if x == 9 and y == 10:
        if check_empty(board):
            ans = min(ans, cnt)
        return

    if y == 10:
        dfs(x + 1, 0, cnt)
        return

    if cnt >= ans:
        return

    if board[x][y] == 0:
        dfs(x, y + 1, cnt)

    else:
        for i in range(4,-1,-1):  # (4,3,2,1,0)
            if paper[i] == 0: # 남은 색종이가 없으면
                continue

            if x + i >= 10 or y + i >= 10:  # 색종이가 종이를 뚫고 나가는지
                continue

            if check_paper(x, y, board, i):
                for a in range(x, x + 1 + i):
                    for b in range(y, y + 1 + i):
                        board[a][b] = 0
                paper[i] -= 1
                dfs(x, y + 1, cnt + 1)
                for a in range(x, x + 1 + i):
                    for b in range(y, y + 1 + i):
                        board[a][b] = 1
                paper[i] += 1

if check_empty(board):
    print(0)
    exit()

dfs(0,0,0)

print(-1) if ans == 101 else print(ans)

