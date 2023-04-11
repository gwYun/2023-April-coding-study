from copy import deepcopy
from itertools import combinations
N, M, D = map(int,input().split())
graph = []
counters = []
for i in range(N):  
    graph.append(list(map(int,input().split())))
    for j in range(M):
        if graph[i][j]==1:
            counters.append([i,j])

# 궁수 = 3명 / m 개의 칸에 들어갈 수 있음

max_dels = 0
def simulation(teams,counters): # 3개의 위치 
    global max_dels
    total_dels= 0
    c = 0
    while counters:
        dels = []
        for team in teams :
            min_dist = int(1e9)
            min_index = -1
            min_x = -1
            dist_info = []
            for i, count in enumerate(counters):
                dist =  abs(N-count[0])+abs(team-count[1])
                if dist <=D:
                    dist_info.append([dist,counters[i][0],i])
                '''
                if dist <=D and min_dist>=dist:
                    if min_dist==dist:
                        if min_x > counters[i][0]:
                            min_index =i 
                            min_x = counters[i][0]
                    else:
                        min_dist = dist
                        min_index=i'''
                        
            if len(dist_info)==0:
                continue
            else:
                dist_info = sorted(dist_info,key = lambda x:(x[0],x[1]))
                print(dist_info)
                dels.append(dist_info[0][2])
                '''
            if min_index==-1:
                #죽일게 없다는 말 
                continue
            else:
                dels.append(min_index)'''
        
        for k in list(set(dels))[::-1]:
            counters = counters[:k]+counters[k+1:]
        # 삭제한 개수 추가 
        total_dels+=len(list(set(dels)))
        
        
        # 가까운 곳 공격 후 아래로 움직임 
        counters = move(counters)
        c+=1
        print(c, dels,total_dels)
        print(counters)

    max_dels = max(max_dels,total_dels)
    
    
def move(counters):

    dels = []
    for i in range(len(counters)):
        counters[i][0]+=1
        if counters[i][0]>=N:
            dels.append(i)
            
    for k in dels[::-1]:
        counters = counters[:k]+counters[k+1:]
        
    return counters



cases = list(combinations(range(M), 3))
simulation((2,6,9),counters)
for case in cases:
    cnts = deepcopy(counters)
    simulation(case,cnts)
print(max_dels)





########### 반례 
# 
"""
9 10 4
1 0 0 1 0 1 0 1 1 0
0 0 0 1 0 0 0 1 0 0
0 1 0 0 1 0 0 1 1 1
0 0 1 1 0 1 0 1 1 0
0 1 1 0 0 0 0 1 0 1
0 1 1 1 0 1 0 1 0 0
0 0 0 0 0 0 0 1 0 0
1 1 1 1 1 1 1 1 0 1
0 1 1 0 1 1 0 1 1 0
answer

26

input

2 4 2

1 1 1 1

0 1 1 0

output

6

answer

5

input

4 5 2
1 0 0 1 1
0 1 1 1 0
1 1 1 0 0
1 0 1 0 1

output

12

answer

11

input

9 10 4
1 0 0 1 0 1 0 1 1 0
0 0 0 1 0 0 0 1 0 0
0 1 0 0 1 0 0 1 1 1
0 0 1 1 0 1 0 1 1 0
0 1 1 0 0 0 0 1 0 1
0 1 1 1 0 1 0 1 0 0
0 0 0 0 0 0 0 1 0 0
1 1 1 1 1 1 1 1 0 1
0 1 1 0 1 1 0 1 1 0

output

34

answer

26

"""