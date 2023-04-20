from itertools import permutations

def check(user,ban): # 해당아이디랑 불량사용자 아이디를 비교
    if len(user) != len(ban):
        return False

    for i in range(len(ban)):
        if ban[i] == '*':
            continue
        if user[i] != ban[i]:
            return False
    
    return True

def solution(user_id, banned_id):
    ans = []
    for user in permutations(user_id, len(banned_id)): # 밴 된 아이디에 대응 되는 경우의수 탐색
        cnt = 0
        for i in range(len(banned_id)):
            if check(user[i], banned_id[i]):
                cnt += 1 # 불량 사용자 인경우
            
        if cnt == len(banned_id):
            if set(user) not in ans:
                ans.append(set(user))
    
    return len(ans)
            
