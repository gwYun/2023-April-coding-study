n = 10
보드 = [list(map(int, input().split())) for _ in range(n)]

색종이 = [0, 5, 5, 5, 5, 5]

색종이_최솟값 = int(1e9)

def 붙일수있는지(보드, x, y, 크기):
    for i in range(x, x + 크기):
        for j in range(y, y + 크기):
            if i >= n or j >= n or 보드[i][j] == 0:
                return False
    return True

def detach(보드, x, y, 크기, 값):
    for i in range(x, x + 크기):
        for j in range(y, y + 크기):
            보드[i][j] = 값

def dfs(보드, 색종이, 현재갯수):
    global 색종이_최솟값

    if 현재갯수 >= 색종이_최솟값:
        return

    if sum(sum(row) for row in 보드) == 0:
        색종이_최솟값 = min(색종이_최솟값, 현재갯수)
        return

    x, y = -1, -1
    for i in range(n):
        for j in range(n):
            if 보드[i][j] == 1:
                x, y = i, j
                break
        if x != -1:
            break

    if x == -1:
        return

    for 크기 in range(1, 6):
        if 색종이[크기] > 0 and 붙일수있는지(보드, x, y, 크기):
            색종이[크기] -= 1
            detach(보드, x, y, 크기, 0)
            dfs(보드, 색종이, 현재갯수 + 1)
            색종이[크기] += 1
            detach(보드, x, y, 크기, 1)

dfs(보드, 색종이, 0)
print(색종이_최솟값 if 색종이_최솟값 != int(1e9) else -1)