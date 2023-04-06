'''''
2020 카카오 인턴십 - 2. 수식 최대화
https://school.programmers.co.kr/learn/courses/30/lessons/67257
'''
from collections import deque
from itertools import permutations


def solution(expression):
    prev, mx = -1, -1
    num_ops, op_types = [], set()
    for i, ch in enumerate(expression):
        if ch == '*' or ch == '+' or ch == '-':
            num_ops.extend([int(expression[prev + 1: i]), ch])
            op_types.add(ch)
            prev = i
    num_ops.append(int(expression[prev + 1:]))

    permus = permutations(op_types)
    for p in permus:
        s1, s2 = deque([]), deque(num_ops)
        for cur_op in p:
            while s2:
                cur = s2.popleft()
                s1.append(eval(f'{s1.pop()} {cur} {s2.popleft()}') if cur == cur_op else cur)
            s1, s2 = s2, s1
        mx = max(mx, abs(s2[0]))
    return mx


if __name__ == '__main__':
    print(solution("100-200*300-500+20"))
    print(solution("50*6-3*2"))