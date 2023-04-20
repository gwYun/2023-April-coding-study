'''''
2019 카카오 개발자 겨울 인턴십 - 불량 사용자
https://school.programmers.co.kr/learn/courses/30/lessons/64064
'''

from itertools import permutations


def match(id1, id2):
    l1, l2 = len(id1), len(id2)
    if l1 != l2:
        return False
    for i in range(l1):
        if id1[i] != id2[i] and id2[i] != '*':
            return False
    return True


def solution(user_id, banned_id):
    ans = list()
    l = len(banned_id)
    permus = permutations(user_id, l)
    for candidate_ids in permus:  # candidate_ids: ["frodo", "fradi"]
        cnt = sum(match(candidate_ids[i], banned_id[i]) for i in range(l))
        if cnt == l and set(candidate_ids) not in ans:
            ans.append(set(candidate_ids))
    return len(ans)


if __name__ == '__main__':
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
