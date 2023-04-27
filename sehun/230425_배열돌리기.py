#배열연산해서 최솟값구하는함수
#회전연산하는 함수
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
배열 = [list(map(int, input().split())) for _ in range(n)]
회전연산 = [list(map(int,input().split())) for _ in range(k)]
최소 = int(1e9)
방문여부 = [-1] * k

def 회전하기(배열, r, c, s) : # 회전 연산
    for i in range(s) :
        r1, c1, r2, c2 = r-s+i, c-s+i, r+s-i, c+s-i # 가장 왼쪽 위 (r1,c1) 가장 오른쪽 아래 (r2,c2)
        temp = 배열[r1][c1] # 가장 왼쪽 위 값저장
        for idx in range(r1, r2) : # c1열
            배열[idx][c1] = 배열[idx+1][c1]
        for idx in range(c1, c2) : # r2행
            배열[r2][idx] = 배열[r2][idx+1]
        for idx in range(r2,r1,-1) :  # c2열
            배열[idx][c2] = 배열[idx-1][c2]
        for idx in range(c2, c1+1, -1) : # r1행
            배열[r1][idx] = 배열[r1][idx-1]
        배열[r1][c1+1] = temp #가장 왼쪽 위 값저장
    return 배열

def dfs(현재회전, cur) : # 순열로 회전 연산 실행 / 최솟값 찾기
    global 최소
    if 현재회전 == k :
        opelist = [회전연산[idx] for idx in 방문여부]
        임시복사배열 = [i[:] for i in 배열]
        for r, c, s in opelist :
            임시복사배열 = 회전하기(임시복사배열, r-1, c-1, s)
        최소 = min(최소, min([sum(temp) for temp in 임시복사배열]))
        return
    for i in range(k):
        if 방문여부[i] == -1 : #아직 값 못채웠다면
            방문여부[i] = cur # 현재 추가해야 할 인덱스 값 대입
            dfs(현재회전 + 1, cur + 1)
            방문여부[i] = -1    

dfs(0, 0)
print(최소)
  