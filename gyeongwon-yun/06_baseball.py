import sys
# from collections import deque
from itertools import permutations
# import time

def solution(N, hits, skip_max_score_possible):
  
    combs = list(map(list, permutations([1, 2, 3, 4, 5, 6, 7, 8])))
    max_score = 0

    if not skip_max_score_possible:
        #get max score possible for each inning
        max_inning_score = [0]*N
        for inning, h in enumerate(hits):
            h_sorted = list(sorted(h))

            zeros = 0
            while zeros < 9 and h_sorted[0] == 0:
                h_sorted.append(h_sorted.pop(0))
                zeros += 1

            inning_result, _ = get_inning_result(h_sorted, 0)
            max_inning_score[inning] = inning_result

        #get max score possible for the remaining innings
        max_score_possible = [0]*N
        max_score_accumulated = 0
        for i in range(N-1, -1, -1):
            max_score_accumulated += max_inning_score[i]
            max_score_possible[i] = max_score_accumulated

    for c in combs:
        #get player queue
        player_queue = c[:3]+[0]+c[3:]

        #get total score
        score = 0
        player_index = 0
        for inning, expected_hits in enumerate(hits):
            if not skip_max_score_possible and score + max_score_possible[inning] <= max_score:
                break
            out = 0
            b1, b2, b3 = False, False, False
            while out < 3:      
                # hit_result = hits[i]
                if expected_hits[player_queue[player_index]] == 0:
                    out += 1
                elif expected_hits[player_queue[player_index]] == 1:
                    score, b3, b2, b1 = score + b3, b2, b1, True
                elif expected_hits[player_queue[player_index]] == 2:
                    score, b3, b2, b1 = score + b3 + b2, b1, True, False
                elif expected_hits[player_queue[player_index]] == 3:
                    score, b3, b2, b1 = score + b3 + b2 + b1, True, False, False
                elif expected_hits[player_queue[player_index]] == 4:
                    score, b3, b2, b1 = score + b3 + b2 + b1 + 1, False, False, False
                
                player_index = (player_index+1)%9
        
        if score > max_score:
            max_score = score
            
    return max_score
    
def get_inning_result(hits, starting_idx):
    score = 0
    out = 0
    i = starting_idx
    b1, b2, b3 = False, False, False
    while out < 3:      
        # hit_result = hits[i]
        if hits[i] == 0:
            out += 1
        elif hits[i] == 1:
            score, b3, b2, b1 = score + b3, b2, b1, True
        elif hits[i] == 2:
            score, b3, b2, b1 = score + b3 + b2, b1, True, False
        elif hits[i] == 3:
            score, b3, b2, b1 = score + b3 + b2 + b1, True, False, False
        elif hits[i] == 4:
            score, b3, b2, b1 = score + b3 + b2 + b1 + 1, False, False, False
        
        i = (i+1)%9
    return score, i
            

input = sys.stdin.readline
N = int(input())
hits = [list(map(int, input().split())) for _ in range(N)]

# print(N, *hits, sep='\n')
# start_time = time.time()
print(solution(N, hits, False))
# print("--- %s seconds without max_possible ---" % (time.time() - start_time))

# start_time = time.time()
# print(solution(N, hits, False))
# print("--- %s seconds with max_possible (expected to be faster) ---" % (time.time() - start_time))

'''
45
1 2 4 3 0 2 1 0 3
1 2 1 2 0 0 0 0 1
3 4 2 3 1 2 3 4 0
0 1 2 3 4 2 1 0 0
0 0 0 0 0 0 1 4 4
0 4 0 4 0 4 0 4 0
0 4 2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 0
0 2 0 3 0 1 0 2 0
1 2 4 3 0 2 1 0 3
1 2 1 2 0 0 0 0 1
3 4 2 3 1 2 3 4 0
0 1 2 3 4 2 1 0 0
0 0 0 0 0 0 1 4 4
0 4 0 4 0 4 0 4 0
0 4 2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 0
0 2 0 3 0 1 0 2 0
1 2 4 3 0 2 1 0 3
1 2 1 2 0 0 0 0 1
3 4 2 3 1 2 3 4 0
0 1 2 3 4 2 1 0 0
0 0 0 0 0 0 1 4 4
0 4 0 4 0 4 0 4 0
0 4 2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 0
0 2 0 3 0 1 0 2 0
1 2 4 3 0 2 1 0 3
1 2 1 2 0 0 0 0 1
3 4 2 3 1 2 3 4 0
0 1 2 3 4 2 1 0 0
0 0 0 0 0 0 1 4 4
0 4 0 4 0 4 0 4 0
0 4 2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 0
0 2 0 3 0 1 0 2 0
1 2 4 3 0 2 1 0 3
1 2 1 2 0 0 0 0 1
3 4 2 3 1 2 3 4 0
0 1 2 3 4 2 1 0 0
0 0 0 0 0 0 1 4 4
0 4 0 4 0 4 0 4 0
0 4 2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 0
0 2 0 3 0 1 0 2 0
'''

