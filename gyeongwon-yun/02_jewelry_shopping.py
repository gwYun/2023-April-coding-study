from collections import deque
import bisect


def solution(gems):
    gems_type = set(gems)
    gems_idx = {}
    for g in gems_type:
        gems_idx[g] = deque([])

    for i, g in enumerate(gems):
        gems_idx[g].append(i)

    min_range = [0, len(gems)]
    next_gems_at = sorted([gems_idx[g][0] for g in gems_type])

    for idx in range(len(gems)-len(gems_type)+1):

        current_gem = gems[idx]
        min_idx = idx
        max_idx = next_gems_at[-1]

        if max_idx-min_idx < min_range[1] - min_range[0]:
            min_range = [min_idx, max_idx]

        gems_idx[current_gem].popleft()
        next_gems_at.pop(0)
        if len(gems_idx[current_gem]) == 0:
            break

        bisect.insort(next_gems_at, gems_idx[current_gem][0])

    return [min_range[0]+1, min_range[1]+1]


def test(gems):
    print(solution(gems))


test(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
test(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
