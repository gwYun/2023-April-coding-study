def solution(numbers, hand):
    # print(numbers, hand)
    distances = {
        2: [3, 1, 0, 1, 2, 1, 2, 3, 2, 3, 4],
        5: [2, 2, 1, 2, 1, 0, 1, 2, 1, 2, 3],
        8: [1, 3, 2, 3, 2, 1, 2, 1, 0, 1, 2],
        0: [0, 4, 3, 4, 3, 2, 3, 2, 1, 2, 1],
    }
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    left = '*'
    right = '#'
    preferred_hand = 'R' if hand == 'right' else 'L'
    answer = ''

    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            left = n
            
        elif n in [3, 6, 9]:
            answer += 'R'
            right = n
            
        else: #n in [2, 5, 8, 0]
            dist_l = 0
            dist_r = 0
            
            #get distance
            if left == '*':
                dist_l = distances[n][10]
            else:
                dist_l = distances[n][left]
                
            if right == '#':
                dist_r = distances[n][10]
            else:
                dist_r = distances[n][right]
                
                
            #if same distance
            if dist_l == dist_r:
                answer += preferred_hand
                if preferred_hand == 'L':
                    left = n
                else:
                    right = n
            
            #different distance
            else:
                if dist_l > dist_r:
                    answer += 'R'
                    right = n
                else:
                    answer += 'L'
                    left = n
                
    return answer

