'''
https://www.acmicpc.net/problem/16637
'''
import sys

sys.stdin = open('../input.txt', 'r')


def dfs(idx, val):
    global mx

    if idx == N - 1:
        mx = max(mx, val)
        return

    if idx + 2 < N:
        # 괄호 추가하지 않은 경우
        dfs(idx + 2, eval(f'{val} {expr[idx + 1]} {int(expr[idx + 2])}'))

    if idx + 4 < N:
        # 괄호 추가한 경우
        tmp = eval(f'{int(expr[idx + 2])} {expr[idx + 3]} {int(expr[idx + 4])}')
        dfs(idx + 4, eval(f'{val} {expr[idx + 1]} {tmp}'))


N = int(input())
expr = str(input())
mx = int(-1e9)

dfs(0, int(expr[0]))
print(mx)
