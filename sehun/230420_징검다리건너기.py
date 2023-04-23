def solution(stones, k):
    left,right = 0, 200000000
    
    while left<=right:
        flag=0
        mid = (left+right) // 2
        
        for stone in stones:
            #연속으로 0이 k개이상인경우 flag에 저정하고 코드종료하는 로직
            if (stone-mid)<=0: flag+=1 
            else: flag=0
            if k<=flag: break #k개이상 빈칸있으면 break
  
        if k<=flag: right = mid - 1
        if k>flag: left = mid + 1

    return left