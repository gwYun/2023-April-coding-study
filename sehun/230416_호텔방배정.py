def solution(k, room_number):
    answer = []
    dic = {}
    
    for want_room in room_number:
        temp = want_room
        visited = [temp]
        while temp in dic:
            temp = dic[temp]
            visited.append(temp)
        answer.append(temp)
        
        for j in visited: #방문한방들 value로 temp+1(미방문방중 가장작은방) 할당해놓기
            dic[j] = temp+1
    return answer