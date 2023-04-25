import sys

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 8)

n = int(input())

arr = input().strip()

ans = -int(1e9)


def calc(num1, op, num2):
    if op == '+': return num1 + num2
    if op == '*': return num1 * num2
    if op == '-': return num1 - num2


def dfs(index, value):
    global ans
    if index == n - 1:
        ans = max(ans, value)
        return

    if index + 2 < n:
        dfs(index + 2, calc(value, arr[index + 1], int(arr[index + 2])))

    if index + 4 < n:
        dfs(index + 4, calc(value, arr[index + 1], calc(int(arr[index + 2]), arr[index + 3], int(arr[index + 4]))))

dfs(0, int(arr[0]))

print(ans)
