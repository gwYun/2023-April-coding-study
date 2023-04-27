from itertools import permutations
from copy import deepcopy
from pprint import pprint

def rotate(matrix, r, c, s) : # 회전 연산 함수
    for i in range(s) :
        r1, c1, r2, c2 = r-s+i, c-s+i, r+s-i, c+s-i # 가장 왼쪽 윗칸 r,c 가장 오른쪽 아랫칸 r,c 저장
        temp = matrix[r1][c1] # 가장 왼쪽 윗칸 저장
        # c1열
        for idx in range(r1, r2) :
            matrix[idx][c1] = matrix[idx+1][c1]
        # r2행
        for idx in range(c1, c2) :
            matrix[r2][idx] = matrix[r2][idx+1]
        # c2열
        for idx in range(r2,r1,-1) :
            matrix[idx][c2] = matrix[idx-1][c2]
        # r1행
        for idx in range(c2, c1+1, -1) :
            matrix[r1][idx] = matrix[r1][idx-1]
        matrix[r1][c1+1] = temp # 저장한 가장 왼족 윗칸 값을 바로 다음 열에 넣어줌
        
    return matrix
    


'''
def rotate(arr, r,c,S):
    pprint(arr)
    for s in range(1,S+1):
        
        start = arr[r-s][c-s]
        # 1, 왼쪽 업
        for i in range(r-s,r+s):
            print('left up' ,i,c-s,r,c,r+s)
            arr[i][c-s]=arr[i+1][c-s]
            
        # 하단 > 왼쪽으로 1
        for i in range(c-s,c+s):
            print(c,s,c-s,i)
            arr[r+s][i]= arr[r+s][i+1]
            
        # 우측 - >아래로 1
        for i in range(r+s,r-s,-1):
            arr[i][c+s]= arr[i-1][c+s]
            
        # 위측 -> 오른쪽으로 1
        for i in range(c+s, c-s,-1):
            arr[r-s][i] = arr[r-s][i-1]
            
        arr[r-s][c-s+1]=start
        
    pprint(arr)
    
    return arr
    
    

    

def dfs(L, cur) : # 순열을 만들어 회전 연산 실행 후 최솟값을 찾는 함수
    global min_
    if L == K :
        opelist = [operation[idx] for idx in visitied]
        copy_matrix = [m[:] for m in matrix]
        for r, c, s in opelist :
            copy_matrix = rotation(copy_matrix, r-1, c-1, s)
        min_ = min(min_, min([sum(temp) for temp in copy_matrix]))
        return
    for i in range(K):
        if visitied[i] == -1 : # 아직 값을 채우지 않았다면
            visitied[i] = cur # 현재 추가해야 할 인덱스 값 대입
            dfs(L + 1, cur + 1)
            visitied[i] = -1

if __name__=="__main__" :
    N, M, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    operation = [list(map(int, input().split())) for _ in range(K)]

    min_ = 2147000000 # 배열 A의 값을 큰 수로 초기화
    visitied = [-1] * K # 순열 생성을 위한 리스트
    dfs(0, 0)
    print(min_)

'''
N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]  
info = [list(map(int,input().split())) for _ in range(K)]

cases = list(permutations(info, K))
min_val = int(1e9)
for case in cases:
    arr2 = deepcopy(arr)
    for r,c,s in case:
        arr2=rotate(arr2,r,c,s)
    for line in arr2:
        min = min(min_val, sum(line))

print(min_val)
        
    
