import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())

record = []

for _ in range(n):
    record.append(list(map(int, input().split())))
ans = 0
for seq in permutations([i for i in range(1, 9)], 8):
    seq = list(seq)
    seq.insert(3, 0)  # 타자 순열
    score = 0
    cur = 0 # 타자번호
    for time in range(n):  # n이닝
        out = base1 = base2 = base3 = 0 # 매이닝 마다 아웃카운트, 베이스 초기화
        while out < 3:
            if record[time][seq[cur]] == 0:
                out += 1

            elif record[time][seq[cur]] == 1:
                score += base3
                base3 = base2
                base2 = base1
                base1 = 1

            elif record[time][seq[cur]] == 2:
                score += (base3 + base2)
                base3 = base1
                base2 = 1
                base1 = 0

            elif record[time][seq[cur]] == 3:
                score += (base3 + base2 + base1)
                base3 = 1
                base2 = 0
                base1 = 0
            else:
                score += (base3 + base2 + base1 + 1)
                base1 = base2 = base3 = 0

            cur = (cur + 1) % 9

    ans = max(ans,score)
print(ans)
