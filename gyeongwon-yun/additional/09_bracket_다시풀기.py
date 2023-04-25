import sys

def solution(N, equation):
    global n, numbers, operators, bracketed_numbers, max_val
    n = N//2 + 1 # number of numbers
    numbers = []
    operators = []
    bracketed_numbers = []

    for i in range(N):
        if i%2==0: #number
            numbers.append(int(equation[i]))
        else: #operator
            operators.append(equation[i])
    # print(numbers, operators)

    for i in range(len(operators)):
        bracketed_numbers.append(calc(numbers[i], numbers[i+1], operators[i]))
    # print(bracketed_numbers)

    max_val = -2^31
    dfs(numbers[0], 1)
    
    return max_val

def dfs(calculated_val, idx):
    global n, numbers, operators, bracketed_numbers, max_val

    if idx >= n: #calculated everything
        max_val = max(calculated_val, max_val)
        return
    
    else:
        dfs(calc(calculated_val, numbers[idx], operators[idx-1]), idx+1)
        if idx < n-1: #two or more numbers left
            dfs(calc(calculated_val, bracketed_numbers[idx], operators[idx-1]), idx+2)
    

def calc(a, b, o):
    if o == '+':
        return a + b
    elif o == '-':
        return a - b
    elif o == '*':
        return a * b

input = sys.stdin.readline
N = int(input())
equation = input()

print(solution(N, equation))