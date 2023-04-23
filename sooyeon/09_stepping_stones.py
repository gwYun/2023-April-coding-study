'''
2019 카카오 개발자 겨울 인턴십 - 징검다리 건너기
https://school.programmers.co.kr/learn/courses/30/lessons/64062
'''


def get_n_zero(arr, k, m):
    cnt = 0
    for e in arr:
        if e <= m:
            cnt += 1
        else:
            if cnt >= k:
                return cnt
            cnt = 0
    return cnt


def solution(stones, k):
    s, e = 1, 200_000_000
    while s <= e:
        mid = (s + e) // 2
        n_zero = get_n_zero(stones, k, mid)
        if n_zero >= k:
            e = mid - 1
        else:
            s = mid + 1
    return s


if __name__ == '__main__':
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
