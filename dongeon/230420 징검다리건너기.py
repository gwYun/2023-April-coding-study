def solution(stones, k):    
    left = 0
    right = max(stones)
    ans = 0
    while left <= right:
        mid = (left + right)//2 # 건널 사람 숫자      
        cnt = 0
        
        for i in stones:
            if i - mid <= 0:
                cnt += 1
            else:
                cnt = 0
        
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
            ans = mid
        else:            
            
            left = mid + 1
    return ans