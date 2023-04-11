import sys
from itertools import combinations
import copy

input = sys.stdin.readline

# 궁수를 3명 배치 mC3
# 궁수는 D이하인 적 중에서 가장 가까운 적 공격
# 거리가 같으면 왼쪽부터, 중복가능 y가 작은게 먼저
# 공격 받은 적 cnt
# 적 한칸씩 이동
# 적이 castle에서 사라지면 게임 종료
# 제거 할수 있는 적의 최댓값

n, m, d = map(int, input().split())
_map = []
ans = 0

for _ in range(n):
    _map.append(list(map(int, input().split())))

def find(combi, castle): # 각 궁수들의 위치 마다 사정거리 안의 적들의 좌표 
    arr = []
    for c in combi:
        enemy = [] 
        for i in range(n):
            for j in range(m):
                if castle[i][j] == 1 and abs(n - i) + abs(c - j) <= d:
                    enemy.append((abs(n - i) + abs(c - j), i, j))

        arr.append(enemy)
    return arr


def attack(arr, castle):  # 적 제거
    removed = set() # 적이 중복되서 제거 될수도 있으므로
    for candi in arr:
        if not candi:
            continue
        candi.sort(key=lambda x: (x[0], x[2]))  # 거리가 짧은순, y 좌표가 작은순
        removed.add((candi[0][1], candi[0][2]))
        castle[candi[0][1]][candi[0][2]] = 0
    return len(removed)


def move_castle(castle):
    for i in range(n - 1, 0, -1):
        castle[i] = castle[i - 1]

    castle[0] = [0] * m


def check_empty(castle):
    for i in range(n):
        for j in range(m):
            if castle[i][j] == 1:
                return False
    return True


for c in combinations([i for i in range(m)], 3):
    castle = copy.deepcopy(_map)
    cnt = 0
    while not check_empty(castle):
        arr = find(c, castle)
        cnt += attack(arr, castle)
        move_castle(castle)

    ans = max(ans, cnt)

print(ans)

