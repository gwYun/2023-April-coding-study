from itertools import permutations
ans = []
def calc(num, op1, op2, op3):
    if len(num) == 1:
        ans.append(abs(num[0]))
        return 
    
    if op1 in num:    
        k = num.index(op1)
        if op1 == '+':
            n = num[k-1] + num[k+1]
        elif op1 == '-':
            n = num[k-1] - num[k+1]
        elif op1 == '*':
            n = num[k-1] * num[k+1]
            
        num.pop(k-1)
        num.pop(k-1)
        num[k-1] = n
        
        calc(num, op1, op2, op3)
    
    elif op2 in num:
        k = num.index(op2)
        if op2 == '+':
            n = num[k-1] + num[k+1]
        elif op2 == '-':
            n = num[k-1] - num[k+1]
        elif op2 == '*':
            n = num[k-1] * num[k+1]        
        
        num.pop(k-1)
        num.pop(k-1)
        num[k-1] = n
        
        calc(num, op1, op2, op3)
    
    elif op3 in num:
        k = num.index(op3)
        if op3 == '+':
            n = num[k-1] + num[k+1]
        elif op3 == '-':
            n = num[k-1] - num[k+1]
        elif op3 == '*':
            n = num[k-1] * num[k+1]
        
        num.pop(k-1)
        num.pop(k-1)
        num[k-1] = n
        
        calc(num, op1, op2, op3)

def solution(expression):
    # 순열 라이브러리를 통해 각각의 우선순위 모든 경우의 수를 다 확인해서 가장 큰값을 정답으로 추출
    operation = list(permutations(['+','*','-']))
    num = []
    c = ''
    
    for i in expression: # expression을 순회하면서 숫자인 경우는 문자열을 합치고 기호면 숫자를 추가한뒤 기호를 추가한다
        if i.isdigit():
            c += i
        else:
            num.append(int(c))
            num.append(i)
            c = ''    
    num.append(int(c)) # num = [100, '-', 200, '*', 300, '-', 500, '+', 20]
    

    for op1,op2,op3 in operation:
        n = num[:]
        calc(n,op1,op2,op3)
    
    return max(ans)