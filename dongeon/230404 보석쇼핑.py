def solution(gems):
    gem_cnt = len(set(gems))
    ans = [1, len(gems)]
    
    start_idx = end_idx = 0
    jew = {gems[0] : 1}

    while start_idx <= end_idx:
        if len(jew) == gem_cnt:
            if end_idx - start_idx < ans[1] - ans[0]:
                ans[0] = start_idx + 1
                ans[1] = end_idx + 1
            
            if jew[gems[start_idx]] > 1:
                jew[gems[start_idx]] -= 1
            else:
                jew.pop(gems[start_idx])
            
            start_idx += 1
        else :
            end_idx += 1       
            if end_idx >= len(gems):
                break
            if end_idx < len(gems):
                if gems[end_idx] in jew:
                    jew[gems[end_idx]] += 1
                else:
                    jew[gems[end_idx]] = 1
            else:
                break
    return ans