def solution(stones, k):
    lives = list(set(stones))
    if len(lives)==1: # all same
        return lives[0]        
    right = max(lives)
    left = 0
    mid = (right + left) // 2
    
    while True:
        jump_dist = 0
        succeed = True
        for s in stones:
            if s < mid: #no_stone
                jump_dist += 1
                if jump_dist >= k: #fail, decrease mid
                    right = mid
                    mid = (left + right) // 2
                    succeed = False
                    break
            else: #yes_stone
                jump_dist = 0
        if succeed: # succedd, increase mid
            left = mid
            mid = (left + right) // 2
        
        if left + 1 == right:
            return mid