def solution(gems):
    N = len(gems)
    answer = [0, N-1]
    딕셔너리비교 = {gems[0]:1,}
    보석갯수 = len(set(gems)) 
    i1,i2 = 0,0  
    
    while i1<N and i2<N:
        if len(딕셔너리비교) < 보석갯수:
            i2 += 1
            if i2 == N:
                break
            딕셔너리비교[gems[i2]] = 딕셔너리비교.get(gems[i2], 0) + 1
            
        else:
            if (i2-i1+1) < (answer[1]-answer[0]+1):
                answer = [i1,i2]
            if 딕셔너리비교[gems[i1]] == 1:
                del 딕셔너리비교[gems[i1]]
            else:
                딕셔너리비교[gems[i1]] -= 1
            i1 += 1

    answer[0] += 1
    answer[1] += 1
    return answer