
def operation(expr,target):
        stack = []
        while expr:
            one = expr.pop(0)
            if one==target:
                if target=='+':
                    one = stack.pop(-1) + expr.pop(0)
                elif target=='-':
                    one = stack.pop(-1) - expr.pop(0)
                elif target=='*':
                    one = stack.pop(-1) * expr.pop(0)
            stack.append(one)
        return stack


def get_expr(expression):
    expr = []
    num=''
    for ex in expression:
        if ex in '*-+':
            expr.append(int(num))
            expr.append(ex)
            num = ''
        else:
            num+=ex
    if num:
        expr.append(int(num))
    return expr

def solution(expression):
    answer = 0
    expr = get_expr(expression)
    max_value = 0
    cases = ['+-*','+*-','-+*','-*+','*+-','*-+']
    for case in cases:
        expr2 = expr[:]
        for ex in case:
            expr2= operation(expr2,ex)
        max_value = max(max_value, abs(expr2[0]))
    return max_value
