'''
https://www.acmicpc.net/problem/17136 backtracking
'''
import sys

sys.stdin = open('../input.txt', 'r')


def cover(r, c, l):
    for i in range(r, r + l):
        for j in range(c, c + l):
            board[i][j] = 0


def uncover(r, c, l):
    for i in range(r, r + l):
        for j in range(c, c + l):
            board[i][j] = 1


def get_max_l(r, c):
    mx_l = 1
    for l in range(2, min(10 - r, 10 - c, 5) + 1):
        for i in range(r, r + l):
            for j in range(c, c + l):
                if board[i][j] == 0:
                    return mx_l
        mx_l += 1
    return mx_l


def dfs(cnt):
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                mx_l = get_max_l(i, j)
                for l in range(mx_l, 0, -1):
                    if papers[l]:
                        cover(i, j, l)
                        papers[l] -= 1
                        ans.add(dfs(cnt + 1))
                        uncover(i, j, l)
                        papers[l] += 1
                return min(ans) if ans else -1
    return cnt


ans = set()
board = [list(map(int, input().split())) for _ in range(10)]
papers = [5] * 6
papers[0] = 0

ans.add(dfs(0))
if -1 in ans:
    ans.remove(-1)
print(min(ans) if ans else -1)
