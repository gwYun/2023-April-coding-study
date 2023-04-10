import sys
from itertools import combinations
from copy import deepcopy

# input = sys.stdin.readline()
제거된적 = 0
n, m, d = map(int, input().split())
격자판 = [list(map(int, input().split())) for _ in range(n)]
적위치 = []

for i in range(n):
   for j in range(m):
      if 격자판[i][j]==1: #적있는 인덱스 저장
         적위치.append([i,j])

#성은 n+1번줄, 3명궁수, 성이있는칸. 거리가d인적중 가장가까운적+가장왼쪽

def 가까운적찾기(궁수위치, 적위치):
    좌표 = []
    거리 = int(1e9)
    for 위치 in 적위치:
      temp = abs(위치[0]-궁수위치[0]) + abs(위치[1]-궁수위치[1])
      if temp<= 거리 and temp<=d:
        #같으면 더 왼쪽값을 대입
        if temp == 거리:
          if 좌표[1] > 위치[1]:
              좌표 = 위치[:]
              거리 = temp
        #거리가 더 작으면 무지성대입   
        else:
           좌표 = 위치[:]
           거리 = temp
    return 좌표


for ti in combinations(range(m), 3):
  # print(ti)
  궁수위치 = [[n, ti[0]], [n, ti[1]], [n, ti[2]]]
  임시적위치 = deepcopy(적위치)
  임시제거된적 = 0
  while 임시적위치:
    
    공격할적 = []
    for i in range(3):
      #궁수위치별 가까운적찾기 ㄱㄱ
      공격할적.append(가까운적찾기(궁수위치[i], 임시적위치))
    
    for i in 공격할적: #적공격하기
       if len(i) and i in 임시적위치: #적이 있으면 공격 ㄱㄱ
          임시적위치.remove(i)
          임시제거된적 += 1
    #남은적 있는지 확인
    if not len(임시적위치):
       break
    
    #한턴끝나면 적위치 1++하는 코드
    for i in range(len(임시적위치)):
      임시적위치[i][0] += 1
    #적이 범위 나간경우 리스트에서 제거하는 코드
    t=0
    while t < len(임시적위치):
       if 임시적위치[t][0]>=n:
          del 임시적위치[t]
          t-=1
       t+=1
  
  #while문 끝날때마다 제거된적 업데이트 ㄱ
  제거된적 = max(제거된적, 임시제거된적)

print(제거된적)
