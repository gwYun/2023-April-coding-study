#ref: https://www.acmicpc.net/source/57009296 -> 속도 빨라지는지 확인

from itertools import permutations
num = int(input())
rounds = []
for _ in range(num):
    rounds.append(list(map(int, input().split())))

max_inning_score = [0]*num
for inning, h in enumerate(rounds):
    h_sorted = list(sorted(h))

    zeros = 0
    while zeros < 9 and h_sorted[0] == 0:
        h_sorted.append(h_sorted.pop(0))
        zeros += 1

    score = 0
    hitter = 0
    first, second, third = 0, 0, 0
    out = 0
    while out < 3:
        step = h_sorted[hitter]
        if step == 0:
            out += 1
        elif step == 1:
            score += first
            first, second, third = second, third, 1
        elif step == 2:
            score += first + second
            first, second, third = third, 1, 0
        elif step == 3:
            score += first + second + third
            first, second, third = 1, 0, 0
        else:
            score += first + second + third + 1
            first, second, third = 0, 0, 0
        hitter = (hitter + 1) % 9
    max_inning_score[inning] = score

#get max score possible for the remaining innings
max_score_possible = [0]*num
max_score_accumulated = 0
for i in range(num-1, -1, -1):
    max_score_accumulated += max_inning_score[i]
    max_score_possible[i] = max_score_accumulated


max = 0
for p in permutations(range(1, 9)):
    p = list(p)
    global order
    order = p[:3] + [0] + p[3:]
    score = 0
    hitter = 0
    for inning, round in enumerate(rounds):
        if score + max_score_possible[inning] <= max:
            break
        first, second, third = 0, 0, 0
        out = 0
        while out < 3:
            step = round[order[hitter]]
            if step == 0:
                out += 1
            elif step == 1:
                score += first
                first, second, third = second, third, 1
            elif step == 2:
                score += first + second
                first, second, third = third, 1, 0
            elif step == 3:
                score += first + second + third
                first, second, third = 1, 0, 0
            else:
                score += first + second + third + 1
                first, second, third = 0, 0, 0
            hitter = (hitter + 1) % 9
    if score > max:
        max = score
print(max)