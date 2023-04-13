##reference: https://brorica.tistory.com/entry/%EB%B0%B1%EC%A4%8017136-%EC%83%89%EC%A2%85%EC%9D%B4-%EB%B6%99%EC%9D%B4%EA%B8%B0-Python3
import math

sizes = [0, 0, 0, 0, 0, 0]
visit = [[False for _ in range(10)] for _ in range(10)]
N = 10
ans = float("inf")
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def main():
    ones = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                ones += 1
    dfs(0,ones)
    if ans == float("inf"):
        print(-1)
    else:
        print(ans)

def dfs(count, ones):
    global ans
    if count >= ans:
        return
    if ones == 0:
        ans = min(ans, sum(sizes))
        return


    for y in range(N):
        for x in range(N):
            if not board[y][x]:
                continue
            for s in range(4, -1, -1):
                if sizes[s + 1] >= 5 or y + s >= N or x + s >= N or not check(y, x, s):
                    continue
                fill(y, x, s)
                dfs(count + 1, ones-((s+1)**2))
                restore(y, x, s)
            return

def fillCheck():
    for y in range(N):
        for x in range(N):
            if board[y][x]:
                return False
    return True

def check(Y, X, s):
    for y in range(Y, Y + s + 1):
        for x in range(X, X + s + 1):
            if not board[y][x]:
                return False
    return True

def fill(Y, X, s):
    for y in range(Y, Y + s + 1):
        for x in range(X, X + s + 1):
            board[y][x] = 0
    sizes[s + 1] += 1

def restore(Y, X, s):
    for y in range(Y, Y + s + 1):
        for x in range(X, X + s + 1):
            board[y][x] = 1
    sizes[s + 1] -= 1




if __name__ == "__main__":
    main()

'''
0 0 0 0 1 1 1 1 1 1
0 1 1 1 1 1 1 1 1 1
0 1 1 1 1 1 1 1 1 1
0 1 1 1 1 1 1 1 1 1
0 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
'''