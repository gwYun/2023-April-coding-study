def solution(numbers, hand):
    result = ''

    nowL,nowR = (3,0), (3,2)
    get_pos = [(3,1),(0,0),(0,1),(0,2),
                    (1,0),(1,1),(1,2),
                    (2,0),(2,1),(2,2)]
    
    for num in numbers:
        pos = get_pos[num]
        if pos[1]==0:answer = 'L'
        elif pos[1]==2:answer = 'R'
        else: # 사이인 경우 거리 계산
            Llen = abs(nowL[0]-pos[0])+pos[1]-nowL[1]
            Rlen = abs(nowR[0]-pos[0])+nowR[1]-pos[1]
            if Llen==Rlen: answer = 'R' if hand=='right' else 'L'
            elif Llen>Rlen:answer = 'R'
            else:answer = 'L'
        if answer=='R':nowR = pos
        else:nowL = pos
        result+=answer
    return result
