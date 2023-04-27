import heapq
from itertools import combinations, permutations
import copy
from collections import deque, defaultdict, Counter
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

board = [[]]

for _ in range(n):
    board.append([0] + list(map(int, input().split())))

op = []

for _ in range(k):
    op.append(list(map(int, input().split())))


# r-s,c-s    r-s,c+s
# r+s,c-s    r+s,c+s


def rotate(o,graph):
    r, c, s = o

    for j in range(s):
        tmp = graph[r - s + j][c - s + j]
        for i in range(r - s + j, r + s - j):# 좌
            graph[i][c - s + j] = graph[i + 1][c - s + j]

        for i in range(c - s + j, c + s-j): # 하
            graph[r + s - j][i] = graph[r + s - j][i+1]

        for i in range(r + s - j, r - s + j, -1): #우
            graph[i][c + s - j] = graph[i - 1][c + s - j]

        for i in range(c + s - j, c - s + j, -1): # 상
            graph[r - s + j][i] = graph[r - s + j][i - 1]

        graph[r - s + j][c - s + 1 + j] = tmp



maxVal = int(1e9)
for z in permutations(op):
    g = copy.deepcopy(board)

    for i in z:
        rotate(i, g)

    for i in range(1,n+1):
        maxVal = min(maxVal, sum(g[i]))

print(maxVal)



