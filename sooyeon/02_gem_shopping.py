'''
2020 카카오 인턴십 - 3. 보석 쇼핑
https://school.programmers.co.kr/learn/courses/30/lessons/67258
'''


def solution(gems):
    n, n_type = len(gems), len(set(gems))
    candi_dict = {}  # 현재 구간의 보석 종류: 개수 저장

    s, e, mn = 0, 0, n
    while s < n and e < n:
        candi_dict[gems[e]] = candi_dict.get(gems[e], 0) + 1

        if len(candi_dict) == n_type:
            while candi_dict[gems[s]] > 1:
                candi_dict[gems[s]] -= 1
                s += 1

            if mn > e - s:
                mn = e - s
                ans = [s + 1, e + 1]
        e += 1
    return ans


if __name__ == '__main__':
    gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    print(solution(gems))

    gems = ["AA", "AB", "AC", "AA", "AC"]
    print(solution(gems))

    gems = ["XYZ", "XYZ", "XYZ"]
    print(solution(gems))

    gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
    print(solution(gems))