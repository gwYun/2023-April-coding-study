import sys

sys.setrecursionlimit(10**8)

ans = []

def check(number, room):
    if number not in room:
        room[number] = number+1
        ans.append(number)    
        return number
    else:
        new_number = check(room[number], room)
        room[number] = new_number+1
        return room[number] - 1
    

def solution(k, room_number):
    room = {}
    
    for i in room_number:
        check(i, room)
        
    return ans