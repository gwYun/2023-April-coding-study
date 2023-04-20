def solution(user_id, banned_id):
    answer = set()

    def 아이디찾기(아이디리스트, 밴아이디):
        리스트 = []
        for idx in range(len(아이디리스트)):
            if len(아이디리스트[idx]) == len(밴아이디):
                flag=1
                for i in range(len(밴아이디)):
                    if 밴아이디[i]=='*': continue # *일경우엔 문자비교 생략
                    if 밴아이디[i] != 아이디리스트[idx][i]: flag=0 #문자 하나라도 틀리면 flag=0 갱신
                if flag: 리스트.append(idx) 
        return 리스트

    
    def 백트래킹(현재밴아이디, 선택된아이디):
        if 현재밴아이디 == len(banned_id):
            answer.add(tuple(sorted(선택된아이디)))
            return

        가능한아이디 = 아이디찾기(user_id, banned_id[현재밴아이디])

        for 아이디 in 가능한아이디:
            if 아이디 not in 선택된아이디:
                선택된아이디.add(아이디)
                백트래킹(현재밴아이디 + 1, 선택된아이디)
                선택된아이디.remove(아이디)

    백트래킹(0, set())
    return len(answer)