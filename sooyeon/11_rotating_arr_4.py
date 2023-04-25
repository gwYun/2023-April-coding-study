'''
https://www.acmicpc.net/problem/17406
2s+2s번 보는 rotate(3576ms)보다 s번만 보면 되는 rotate1이 훨씬 빠름 (760ms)
'''
import sys

sys.stdin = open('../input.txt', 'r')

from copy import deepcopy
from itertools import permutations


def print_arr(arr):
    N = len(arr)
    for i in range(N):
        print(*arr[i])
    print()


def get_score(arr):
    global mn
    N = len(arr)
    for i in range(N):
        mn = min(mn, sum(arr[i]))


def rotate(arr, r, c, s):
    new_arr = deepcopy(arr)

    # ->
    j = c - s
    l = 2 * s
    for i in range(r - s, r):
        new_arr[i][j + 1: j + 1 + l] = arr[i][j: j + l]
        j += 1
        l -= 2

    # <-
    j = c - 1
    l = 2
    for i in range(r + 1, r + s + 1):
        new_arr[i][j: j + l] = arr[i][j + 1: j + l + 1]
        j -= 1
        l += 2

    # up
    ii = r - s
    l = 2 * s
    for j in range(c - s, c):
        for i in range(ii, ii + l):
            new_arr[i][j] = arr[i + 1][j]
        ii += 1
        l -= 2

    # down
    ii = r
    l = 2
    for j in range(c + 1, c + s + 1):
        for i in range(ii, ii + l):
            new_arr[i][j] = arr[i - 1][j]
        ii -= 1
        l += 2

    return new_arr


def rotate1(arr, r, c, s):
    for n in range(s, 0, -1):
        tmp = arr[r - n][c + n]
        arr[r - n][c - n + 1: c + n + 1] = arr[r - n][c - n: c + n]
        for i in range(r - n, r + n):
            arr[i][c - n] = arr[i + 1][c - n]
        arr[r + n][c - n: c + n] = arr[r + n][c - n + 1: c + n + 1]
        for i in range(r + n, r - n, -1):
            arr[i][c + n] = arr[i - 1][c + n]
        arr[r - n + 1][c + n] = tmp
    return arr


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ops = [list(map(int, input().split())) for _ in range(K)]

mn = float('inf')
permus = permutations(ops, K)
for p in permus:
    arr = deepcopy(A)
    for r, c, s in p:
        r, c = r - 1, c - 1
        arr = rotate1(arr, r, c, s)
    get_score(arr)
print(mn)
