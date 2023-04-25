n = int(input())
수식 = input()
최대결과 = -int(1e9)

def 계산하기(n1, op, n2):
    if op == '+': return n1 + n2
    if op == '-': return n1 - n2
    if op == '*': return n1 * n2

def dfs(i, v):
    global 최대결과

    if i == n-1:
        최대결과 = max(최대결과, v)
        return
    if i + 2 < n:
        dfs(i + 2, 계산하기(v, 수식[i + 1], int(수식[i + 2])))
    if i + 4 < n:
        dfs(i + 4, 계산하기(v, 수식[i + 1], 계산하기(int(수식[i + 2]), 수식[i + 3], int(수식[i + 4]))))

dfs(0, int(수식[0]))
print(최대결과)