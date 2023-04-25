import sys

def solution(N, equation):
    global n
    n = N//2 + 1 # number of numbers
    # global numbers, operators
    numbers = []
    operators = []

    for i in range(N):
        if i%2==0: #number
            numbers.append(int(equation[i]))
        else: #operator
            operators.append(equation[i])
    # print(numbers, operators)

    even_bracket = True
    global bracket_positions
    bracket_positions = []
    add_bracket_positions([False]*n, 0,even_bracket)
    # print(len(bracket_positions), sep='\n')
        
    answer = calculate_eq(numbers, operators)
    
    for p in bracket_positions:
        # print(p)
        result_numbers = []
        result_operators = []
        is_bracket_closed = True
        numbers_in_bracket = []
        operators_in_bracket = []
        for i, is_bracket in enumerate(p):
            if is_bracket:
                is_bracket_closed = not is_bracket_closed
            numbers_in_bracket.append(numbers[i])
            if not is_bracket_closed:
                operators_in_bracket.append(operators[i])
            if is_bracket_closed:
                result_numbers.append(calculate_eq(numbers_in_bracket, operators_in_bracket))
                numbers_in_bracket = []
                operators_in_bracket = []
                if i != n-1: # not end of equation
                    result_operators.append(operators[i])
        # print('final eq:', result_numbers, result_operators)
        answer = max(answer, calculate_eq(result_numbers, result_operators))

    return answer

def calculate_eq(numbers, operators):
    ret = numbers[0]
    for i, o in enumerate(operators):
        ret = calc(ret, numbers[i+1], o)
    return ret

def add_bracket_positions(brackets, bracket_start, even_bracket):
    global n

    if even_bracket:
        global bracket_positions
        bracket_positions.append(brackets)

    for i in range(bracket_start, n-1):
        new_brackets = brackets.copy()
        new_brackets[i] = True
        new_brackets[i+1] = True
        add_bracket_positions(new_brackets, i+2, even_bracket)
    

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

# print(N, equation)
print(solution(N, equation))