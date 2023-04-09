def solution(gems):
    N= len(gems)
    answer = [0,N-1]
    kind = len(set(gems))
    dic = {gems[0]:1}
    s,e, = 0,0
    while s<N and e<N:
        if len(dic)<kind: # 종류가 부족하면 end포인트 증가하고, 
            e+=1
            if e==N:
                break
            dic[gems[e]] = dic.get(gems[e],0)+1
            #
            
        else: # 종류는 부족하지 않으면 ans 비교해서 답 갱신, start point 증가, dic 개수 다운
            if(e-s+1) < (answer[1] - answer[0]+1):
                answer = [s,e]
            if dic[gems[s]] ==1 : # 그 종류가 하나밖에 없으면 
                del dic[gems[s]] # 딕셔너리에서 원소 삭제하고 
            else:
                dic[gems[s]]-=1 # 하나는 아니면 수만 줄인다. 
            s+=1
            
    answer[0]+=1
    answer[1]+=1
    return answer