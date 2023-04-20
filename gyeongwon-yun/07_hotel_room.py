def solution(k, room_number):
    room_number = [(n, i) for i, n in enumerate(room_number)]
    
    answer = [0 for _ in range(len(room_number))]
    next_available = {}
    # for i in range(k+1):
    #     next_available[i] = i
    
    for n, i in room_number:
        next = n
        visited = [n]
        while next_available.get(next): 
            next = next_available[next]
            visited.append(next)

        answer[i] = next
        next_available[n] = next+1

        for j in visited:
            next_available[j] = next+1

    
    return answer

def test(k, room_number):
    print(solution(k, room_number))

test(10,	[1,3,4,1,3,1])