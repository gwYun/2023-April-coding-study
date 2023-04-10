from itertools import permutations
def solution(expression):
    answer = 0
    연산자들 = ['*', '-','+','/']
    사용된연산자 = []
    수식정리 = []
    temp = ''
    
    #수식을 리스트로 정리하기
    for i in expression:
        if i in 연산자들:
            수식정리.append(temp)
            temp = ''
            수식정리.append(i)
            사용된연산자.append(i)
        else:
            temp += i
    수식정리.append(temp)
    
    원본수식정리 = 수식정리[:]
    
    사용된연산자 = list(set(사용된연산자))
    for 경우의수 in permutations(사용된연산자):
        수식정리 = 원본수식정리[:]
        for 연산자 in 경우의수: 
            while 연산자 in 수식정리:
                t = 수식정리.index(연산자)
                수식정리[t+1] = eval(str(수식정리[t-1])+수식정리[t]+str(수식정리[t+1]))
                수식정리 = 수식정리[:t-1] + 수식정리[t+1:]
        answer = max(abs(수식정리[0]), answer)

    return answer