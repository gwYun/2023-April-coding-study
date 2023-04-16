'''
https://www.acmicpc.net/problem/17281
'''
import sys

sys.stdin = open('../input.txt', 'r')

from itertools import permutations

N = int(input())
res = [list(map(int, input().split())) for _ in range(N)]
permus = map(list, permutations(range(2, 10), 8))

mx_score = -1
for p in permus:
    order = p[:3] + [1] + p[3:]  # [9, 8, 7, 1, 4, 6, 3, 2, 5]
    score = 0
    idx = 0

    for inning in range(N):
        out = 0
        base1, base2, base3 = False, False, False
        while out < 3:
            batter = order[idx]
            if res[inning][batter - 1] == 0:
                out += 1
            elif res[inning][batter - 1] == 1:
                score += base3
                base1, base2, base3 = True, base1, base2
            elif res[inning][batter - 1] == 2:
                score += base2 + base3
                base1, base2, base3 = False, True, base1
            elif res[inning][batter - 1] == 3:
                score += base1 + base2 + base3
                base1, base2, base3 = False, False, True
            elif res[inning][batter - 1] == 4:
                score += base1 + base2 + base3 + 1
                base1, base2, base3 = False, False, False
            idx += 1
            if idx == 9:
                idx = 0

    if mx_score < score:
        mx_score = score
print(mx_score)
