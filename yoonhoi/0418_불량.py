from itertools import permutations
def check(pos,ban):
    if len(pos)!=len(ban):
        return False
    
    for p,b  in zip(pos,ban):
        if b=='*':
            continue
        elif p==b:
            continue
        else:
            return False
        
    return True

def solution(user_id, banned_id):
    answer = []
    possibles = permutations(user_id,len(banned_id))
    for possible in possibles:
        flag=True
        for pos,ban in zip( possible,banned_id):
            if not check(pos,ban) : 
                flag=False
        if flag:
            answer.append(sorted(possible))
    answer = list(set(answer))
    print(answer)
    return len(answer)