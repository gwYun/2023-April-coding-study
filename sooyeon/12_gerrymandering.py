'''
https://www.acmicpc.net/problem/17471
'''
import sys

sys.stdin = open('../input.txt', 'r')

from collections import defaultdict, deque
from itertools import combinations


def bfs(group):
    global adj, vis, nums

    dq = deque([group[0]])
    vis[group[0]] = True
    total = nums[group[0] - 1]

    while dq:
        cur = dq.popleft()
        for nx in adj[cur]:
            if not vis[nx] and nx in group:
                dq.append(nx)
                vis[nx] = True
                total += nums[nx - 1]

    return total


mn = float('inf')

N = int(input())
nums = list(map(int, input().split()))

adj = defaultdict(list)
for i in range(N):
    tmp = list(map(int, input().split()))
    adj[i + 1].extend(tmp[1:])

for i in range(1, N // 2 + 1):
    combis = combinations(range(1, N + 1), i)
    for combi in combis:
        not_combi = list(set(range(1, N + 1)) - set(combi))
        vis = [False] * (N + 1)

        a_total = bfs(combi)
        b_total = bfs(not_combi)
        if sum(vis) == N:
            mn = min(mn, abs(a_total - b_total))

print(mn if mn != float('inf') else -1)
